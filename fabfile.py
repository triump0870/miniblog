from os.path import join, dirname, exists, isfile
import string
from random import SystemRandom
import environ
from fabric.api import local, task, abort, settings
from fabric.colors import green


@task()
def build_images():
    django_secret_key = generate_key()
    django_settings_module = get_env_value('DJANGO_SETTINGS_MODULE')
    mysql_pass = get_env_value('DATABASE_PASSWORD')
    print("\nDJANGO_SETTINGS_MODULE: ", django_settings_module)
    print("\n==============Building images==============\n")
    build_mysql_image(mysql_pass)
    build_uwsgi_image(django_secret_key, django_settings_module)
    build_nginx_image()


def get_env_value(key):
    env = environ.Env()
    env_file = join(dirname(__file__), "miniblog/settings/local.env")
    if exists(env_file):
        environ.Env.read_env(str(env_file))

    return env('%s' % key)


@task()
def up():
    example_file_conversion("miniblog.settings.local.env.example")
    local('docker-compose up -d')


@task()
def status():
    local('docker-compose ps')


@task()
def logs(container='miniblog-uwsgi'):
    local('docker logs %s' % container)


@task()
def bash(container='miniblog-uwsgi'):
    local('docker exec -it %s bash' % container)


@task()
def down():
    local('docker-compose down')


@task()
def restart():
    down()
    up()
    try:
        clean()
    except:
        pass
    status()


@task()
def clean():
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


def build_uwsgi_image(django_secret_key, django_settings_module):
    if django_secret_key is None:
        abort("Please provide the django_secret_key; Usage: fab build_uwsgi_image:"
              "django_secret_key='^141&epfu9xc1)ou_^qnx$uo4-z*n3a#s=d2lqutulog2o%!yu'"
              "django_settings_module='miniblog.settings.development")

    if django_settings_module is None:
        abort("Please provide the django_settings_module; Usage: fab build_uwsgi_image:"
              "django_secret_key='^141&epfu9xc1)ou_^qnx$uo4-z*n3a#s=d2lqutulog2o%!yu'"
              "django_settings_module='miniblog.settings.development")

    print("\n==============Building miniblog-uwsgi image==============\n")

    local("docker build --build-arg DJANGO_SECRET_KEY={key} --build-arg DJANGO_SETTINGS_MODULE={settings}"
          " -f dockerify/uwsgi/Dockerfile "
          "-t miniblog-uwsgi .".format(key=django_secret_key, settings=django_settings_module))


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


def build_mysql_image(mysql_pass):
    # if mysql_pass is None or mysql_root_pass is None:
    #     abort('Please provide the MYSQL_PASSWORD and MYSQL_ROOT_PASSWORD')

    print("\n==============Building miniblog-mysql image==============\n")
    local("docker build --build-arg MYSQL_PASSWORD={} -f dockerify/mysql/Dockerfile -t miniblog-mysql .".format(
        mysql_pass))
