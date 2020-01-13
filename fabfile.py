import shutil
import string
import sys
from os import makedirs, walk
from os.path import join, dirname, exists, isfile, getsize, relpath
from random import SystemRandom

import environ
from fabric.api import local, task, abort, settings
from fabric.colors import green


@task()
def build_images():
    if not get_debug_value():
        try:
            backup_database()
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
    build_web_image(django_secret_key)
    build_nginx_image()
    build_celery_image()


def get_env_value(key):
    env = environ.Env()
    env_file = join(dirname(__file__), "miniblog/settings/local.env")
    if exists(env_file):
        environ.Env.read_env(str(env_file))

    return env('%s' % key)


@task()
def up(detached=False):
    if 'mysql_data' != local('docker volume ls -f name=mysql_data -q'):
        create_mysql_volume()
    print("\n===============Volume mysql-data exist, skipping==============\n")
    example_file_conversion("miniblog.settings.local.env.example")
    local('docker-compose up {}'.format('-d' if detached else ''))


def create_mysql_volume():
    print("\n===============Creating mysql-data volume==============\n")
    local('docker volume create --name=mysql_data')


@task()
def status():
    local('docker-compose ps')


@task()
def logs(container='web'):
    local('docker logs %s' % container)


@task()
def bash(container='web', command=""):
    local('docker exec -it %s bash %s' % (container, command))


@task()
def down():
    local('docker-compose down')


@task()
def restart():
    print("\n===============Rebooting the containers==============\n")
    if not get_debug_value():
        backup_database()

    print("\n===============Shutting down the container===============\n")
    down()

    print("\n===============Containers are starting up===============\n")
    up()
    clean()
    print("\n===============The status of the containers===============\n\n   ")
    status()

    if not get_debug_value():
        restore_database()


@task()
def restore_database():
    print("\n===============Restoring Database server===============\n")
    try:
        local('docker exec -it web bash -c "python ./dockerify/web/restore.py"')
    except Exception as ex:
        print("Error occurred: while restoring up the database")
        print("Error details: %s" % ex.message)
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
def reboot(container="web"):
    local('docker restart %s' % container)


@task()
def backup_database():
    print("\n===============Backing up database server to S3===============\n")
    try:
        local('docker exec -it web bash ./dockerify/web/backup.sh')
    except Exception as ex:
        print("Error occurred: while backing up the database")
        print("Error details: %s" % ex.message)
        pass


def build_django_image():
    print("\n==============Building miniblog image==============\n")
    local("docker build -f dockerify/django/Dockerfile -t miniblog .")


def build_web_image(django_secret_key):
    if django_secret_key is None:
        abort("Please provide the django_secret_key; Usage: fab build_web_image:"
              "django_secret_key='^141&epfu9xc1)ou_^qnx$uo4-z*n3a#s=d2lqutulog2o%!yu'"
              "django_settings_module='miniblog.settings.development")

    print("\n==============Building web image==============\n")

    local("docker build --build-arg DJANGO_SECRET_KEY={key} "
          "-f dockerify/web/Dockerfile "
          "-t web .".format(key=django_secret_key))


def build_nginx_image():
    print("\n==============Building nginx image==============\n")
    local('docker build -f dockerify/nginx/Dockerfile -t nginx .')


def build_mysql_image(user, password, database):
    print("\n==============Building mysql image==============\n")
    local("docker build --build-arg DATABASE_USER={} --build-arg DATABASE_PASSWORD={} "
          "--build-arg DATABASE={} -f dockerify/mysql/Dockerfile -t mysql ."
          .format(user, password, database))


def build_celery_image():
    print("\n==============Building celery image==============\n")
    local('docker build -f dockerify/celery/Dockerfile -t celery .')


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
    import boto
    from tqdm import tqdm
    from boto.s3.connection import S3Connection

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


@task
def upload_to_s3(bucket_name=None, source_path=None, dest_path=None):
    import boto3
    import mimetypes

    # Fill these in - you get them when you sign up for S3
    AWS_ACCESS_KEY_ID = get_env_value('AWS_S3_USER_KEY')
    AWS_ACCESS_KEY_SECRET = get_env_value('AWS_S3_USER_SECRET')
    bucket_name = get_env_value('AWS_STORAGE_BUCKET_NAME') if not bucket_name else bucket_name

    client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_ACCESS_KEY_SECRET)

    # enumerate local files recursively
    for root, dirs, files in walk(source_path):
        print ("root: ", root, dirs, files)
        for filename in files:
            if filename.startswith('.'):
                continue
            mime_type = mimetypes.MimeTypes().guess_type(filename)[0]
            if mime_type is None:
                mime_type = 'text/plain'

            # construct the full local path
            local_path = join(root, filename)

            # construct the full S3 path
            relative_path = relpath(local_path, source_path)
            s3_path = join(dest_path, relative_path)

            print('Searching "%s" in "%s"' % (s3_path, bucket_name))
            try:
                client.head_object(Bucket=bucket_name, Key=s3_path)
                print("Path found on S3! Skipping %s..." % s3_path)
            except:
                print("Uploading %s..." % s3_path)
                client.upload_file(local_path, bucket_name, s3_path, ExtraArgs={'ContentType': mime_type})
