"""
Django settings for miniblog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
# import keyring
# import getpass
# here() gives us file paths from the root of the system to the directory
# holding the current file.
here = lambda * x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

PROJECT_ROOT = here("..")
# root() gives us file paths from the root of the system to whatever
# folder(s) we pass it starting at the parent directory of the current file.
root = lambda * x: os.path.join(os.path.abspath(PROJECT_ROOT), *x)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
database_name = 'miniblog'
username = 'rohan'
host = 'localhost'
password = 'Amazon@0870'#keyring.get_password(database_name,username)
# while password == None:
#     password=getpass.getpass(database_name+" Password:\n")
#     #Store the password
#     keyring.set_password(database_name,username,password)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'atr6=r@caj6+ir&%dw&1(0mw68^y96s()dvsdg*k_y6o64msvz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
# DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['localhost']
ADMINS = (
    ("Rohan","b4you0870@gmail.com"),
    )
MANAGERS = ADMINS

TEMPLATE_LOADER = (
    'django.template.loader.filesystem.Loader',
    'django.template.loader.app_directories.Loader',
    )

# Application definition
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    )

LOCAL_APPS = (
    'blog',
    )

THIRD_PARTY_APPS = ()
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'miniblog.urls'

WSGI_APPLICATION = 'miniblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': database_name,
        'USER': username,
        'PASSWORD': password,
        'HOST' : host,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
TEMPLATE_DIRS = (
    root("templates"),
    )

LOGGING = {
    'version': 1,
    'disable_existing_loggers':False,
    'filters': {
        'require_debug_false': {
            '()':'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers':{
        'mail_admins':{
            'level':'ERROR',
            'filters':['require_debug_false'],
            'class':'django.utils.log.AdminEmailHandler'
        }
    },
    'logers': {
        'django.request': {
            'handlers':['mail_admins'],
            'level':'ERROR',
            'propagate':True,
        }
    },
}