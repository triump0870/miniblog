# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

# here() gives us file paths from the root of the system to the directory
# holding the current file.
here = lambda * x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)
PROJECT_ROOT = here("..")

# root() gives us file paths from the root of the system to whatever
# folder(s) we pass it starting at the parent directory of the current file.
root = lambda * x: os.path.join(os.path.abspath(PROJECT_ROOT), *x)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'atr6=r@caj6+ir&%dw&1(0mw68^y96s()dvsdg*k_y6o64msvz'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['localhost']

ADMINS = (
    ("Rohan","b4you0870@gmail.com"),
    )

MANAGERS = ADMINS

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
database_name = 'miniblog'
username = 'rohan'
host = 'localhost'
password = 'Amazon@0870'

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

USE_TZ = True

SITE_ID = 1

#Upload files stored here
MEDIA_ROOT = root("..","..","uploads")

#URL that handles the media served by the MEDIA_ROOT
MEDIA_URL = ''

#Absolute path to the directory static files should be collected to.
STATIC_ROOT = root("..","..","static")

#URL prefix for static files.
STATIC_URL = '/static/'

#Additional locations of static files i.e css, js etc
STATICFILES_DIRS = (
    root("..","assets"),
    )

#List of finder classes that know how to find the static files in various locations.
STATCIFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )

#List of callables that know how to import templates from various sources.
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