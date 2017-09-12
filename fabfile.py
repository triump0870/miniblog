import shutil
import string
import sys
from os import makedirs
from os.path import join, dirname, exists, isfile
from random import SystemRandom

import boto
import environ
from boto.s3.connection import S3Connection
from fabric.api import local, task, abort, settings
from fabric.colors import green
from tqdm import tqdm


@task()
def build_images():
    if not get_debug_value():
        try:
            backup_mysql()
        except Exception as e:
            print("Error occurred: %s" % e)
            exit(1)
    django_secret_key = generate_key()
    django_settings_module = get_env_value('DJANGO_SETTINGS_MODULE')
    database_user = get_env_value('DATABASE_USER')
    database_pass = get_env_value('DATABASE_PASSWORD')
    database = get_env_value('DATABASE')
    print("\nDJANGO_SETTINGS_MODULE: ", django_settings_module)
    print("\n==============Building images==============\n")
    build_django_image()
    build_mysql_image(database_user, database_pass, database)
    build_uwsgi_image(django_secret_key)
    build_nginx_image()


def get_env_value(key):
    env = environ.Env()
    env_file = join(dirname(__file__), "miniblog/settings/local.env")
    if exists(env_file):
        environ.Env.read_env(str(env_file))

    return env('%s' % key)


@task()
def up():
    if 'mysql-data' not in local('docker volume ls -f name=mysql-data'):
        create_mysql_volume()
    example_file_conversion("miniblog.settings.local.env.example")
    local('docker-compose up -d')


def create_mysql_volume():
    print("\n===============Creating mysql-data volume==============\n")
    local('docker volume create --name=mysql-data')


@task()
def status():
    local('docker-compose ps')


@task()
def logs(container='miniblog-uwsgi'):
    local('docker logs %s' % container)


@task()
def bash(container='miniblog-uwsgi', command=""):
    local('docker exec -it %s bash %s' % (container, command))


@task()
def down():
    local('docker-compose down')


@task()
def restart():
    print("\n===============Rebooting the containers==============\n")
    if not get_debug_value():
        backup_mysql()

    print("\n===============Shutting down the container===============\n")
    down()

    print("\n===============Containers are starting up===============\n")
    up()
    clean()
    print("\n===============The status of the containers===============\n\n   ")
    status()

    if not get_debug_value():
        restore_mysql()


@task()
def restore_mysql():
    print("\n===============Restoring MySQL server===============\n")
    try:
        local('docker exec -it miniblog-uwsgi bash -c "python ./dockerify/uwsgi/restore.py"')
    except:
        print("Error occurred: while restoring up mysql")
        pass


@task()
def clean():
    print("\n===============cleaning the unused containers===============\n")
    try:
        local('docker rmi -f $(docker images -q -f dangling=true)')
    except:
        pass
    try:
        local('docker volume rm $(docker volume ls -qf dangling=true)')
    except:
        pass


@task()
def reboot(container="miniblog-uwsgi"):
    local('docker restart %s' % container)


@task()
def backup_mysql():
    print("\n===============Backing up MySQL server to S3===============\n")
    try:
        local('docker exec -it miniblog-uwsgi bash ./dockerify/uwsgi/backup.sh')
    except:
        print("Error occurred: while backing up mysql")
        pass


def build_django_image():
    print("\n==============Building miniblog image==============\n")
    local("docker build -f dockerify/django/Dockerfile -t miniblog .")


def build_uwsgi_image(django_secret_key):
    if django_secret_key is None:
        abort("Please provide the django_secret_key; Usage: fab build_uwsgi_image:"
              "django_secret_key='^141&epfu9xc1)ou_^qnx$uo4-z*n3a#s=d2lqutulog2o%!yu'"
              "django_settings_module='miniblog.settings.development")

    print("\n==============Building miniblog-uwsgi image==============\n")

    local("docker build --build-arg DJANGO_SECRET_KEY={key} "
          "-f dockerify/uwsgi/Dockerfile "
          "-t miniblog-uwsgi .".format(key=django_secret_key))


def generate_key():
    return "".join([SystemRandom().choice(string.ascii_letters + string.digits)
                    for _ in range(50)])


def example_file_conversion(example_file):
    actual_file = example_file.split(".example")[0]
    if not exists(actual_file):
        return None

    if isfile(actual_file):
        print(green('%s file already exists. Not copying %s to %s \n' % (actual_file, example_file, actual_file)))

        # Doing this because `diff` package returns exit code 1
        # when there are differences, which causes the script
        # to abort.
        with settings(warn_only=True):
            output = local('diff -w -B -u %s %s' % (actual_file, example_file))

            # Return code of diff will be 1 if files differ else it will 0
            # For errors the code will be greater than 1.
            if output.return_code == 1:
                print(green('%s and %s files differ \n') % (actual_file, example_file))

    else:
        local('cp %s %s' % (example_file, actual_file))


def build_nginx_image():
    print("\n==============Building miniblog-nginx image==============\n")
    local('docker build -f dockerify/nginx/Dockerfile -t miniblog-nginx .')


def build_mysql_image(user, password, database):
    print("\n==============Building miniblog-mysql image==============\n")
    local("docker build --build-arg DATABASE_USER={} --build-arg DATABASE_PASSWORD={} "
          "--build-arg DATABASE={} -f dockerify/mysql/Dockerfile -t miniblog-mysql ."
          .format(user, password, database))


def get_debug_value():
    debug = get_env_value('DEBUG')
    if debug == 'True':
        return True
    else:
        return False


def build_image2(backend_tag=None):
    backend_image_exist = local("docker images -q ")


@task
def local_s3(path=None, bucket_name=None):
    if path is None:
        path = dirname(__file__)
        PATH = join(path, 's3/')
    else:
        if 's3' not in path:
            PATH = join(path, 's3/')
        elif not path.endswith('/'):
            PATH = path + '/'
        else:
            PATH = path

    print("All the S3 folder and files are going to be downloaded on the %s folder." % repr(PATH))
    if exists(PATH):
        res = input("Path exists. Want to delete the path y/n?")
        if res == 'y' or res == 'Y':
            shutil.rmtree(PATH)
        else:
            sys.exit(0)

    conn = S3Connection(get_env_value('AWS_ACCESS_KEY_ID'), get_env_value('AWS_SECRET_ACCESS_KEY'),
                        host=get_env_value('AWS_S3_HOST'))
    if bucket_name is None:
        bucket = conn.get_bucket(get_env_value('AWS_STORAGE_BUCKET_NAME'))
    else:
        try:
            bucket = conn.get_bucket(bucket_name)
        except boto.exception.S3ResponseError:
            print("Bucket %s does not exist" % repr(bucket_name))
            sys.exit(0)

    # go through the list of files
    bucket_list = bucket.list()
    keys = bucket.get_all_keys()
    pbar = tqdm(total=len(keys))
    for key in bucket_list:
        keyString = str(key.key)
        path = PATH + keyString
        pbar.update(1)
        try:
            key.get_contents_to_filename(path)
        except OSError:
            # check if dir exists
            if not exists(path):
                makedirs(path)  # Creates dirs recursively
    pbar.close()
