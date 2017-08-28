"""
Django settings for miniblog project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
from os.path import dirname, join, exists

from django.core.urlresolvers import reverse_lazy
from .celeryconfig import *

# Build paths inside the project like this: join(BASE_DIR, "directory")
BASE_DIR = dirname(dirname(dirname(__file__)))
# Use Django templates using the new Django 1.8 TEMPLATES settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            join(BASE_DIR, 'templates'),
            # insert more TEMPLATE_DIRS here
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Use 12factor inspired environment variables or from a file
import environ

env = environ.Env()

# Ideally move env file should be outside the git repo
# i.e. BASE_DIR.parent.parent
env_file = join(dirname(__file__), 'local.env')
if exists(env_file):
    environ.Env.read_env(str(env_file))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Raises ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = [env('ALLOWED_HOSTS')]
CELERYD_STATE_DB = join(BASE_DIR, "celery_worker_state")

# Application definition
INSTALLED_APPS = (
    'django.contrib.auth',
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'authtools',
    'crispy_forms',
    'easy_thumbnails',
    'django_markdown',
    'disqus',
    'storages',
    'compressor',
    'raven',
    'celery',

    'blog',
)

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

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Crispy Form Theme - Bootstrap 3
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# For Bootstrap 3, change error alert to 'danger'
from django.contrib import messages

MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

# Authentication Settings
AUTH_USER_MODEL = 'auth.User'
LOGIN_REDIRECT_URL = reverse_lazy("profiles:show_self")
LOGIN_URL = reverse_lazy("accounts:login")

THUMBNAIL_EXTENSION = 'png'  # Or any extn for your thumbnails

STATICFILES_FINDER = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

COMPRESS_ENABLED = True
COMPRESS_CSS_HASHING_METHOD = 'content'
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
STATICFILES_DIRS = [join(BASE_DIR, 'assets')]

AWS_STORAGE_BUCKET_NAME = 'miniblog-static'
AWS_CLOUDFRONT_DOMAIN = 'd1igv859hm3llh.cloudfront.net'
AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
AWS_S3_HOST = env("AWS_S3_HOST")
AWS_S3_SECURE_URLS = env('AWS_S3_SECURE_URLS')

MEDIAFILES_LOCATION = 'media'
MEDIA_ROOT = '/%s/' % MEDIAFILES_LOCATION
MEDIA_URL = 'https://%s/%s/' % (AWS_CLOUDFRONT_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'miniblog.storage_backend.custom_storages.MediaStorage'

STATICFILES_LOCATION = 'static'
STATIC_ROOT = '/%s/' % STATICFILES_LOCATION
STATIC_URL = 'http://%s/%s/' % (AWS_CLOUDFRONT_DOMAIN, STATICFILES_LOCATION)
STATICFILES_STORAGE = 'miniblog.storage_backend.custom_storages.StaticStorage'

AWS_IS_GZIPPED = True
COMPRESS_STORAGE = 'miniblog.storage_backend.custom_storages.CacheS3BotoStorage'
COMPRESS_URL = STATIC_URL

EMAIL_USE_TLS = env('EMAIL_USE_TLS')
EMAIL_TO = env('EMAIL_TO')
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = int(env('EMAIL_PORT'))
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_FROM = env('EMAIL_FROM')
EMAIL_BACKEND = env('EMAIL_BACKEND')
DISQUS_API_KEY = env('DISQUS_API_KEY')
DISQUS_WEBSITE_SHORTNAME = env('DISQUS_WEBSITE_SHORTNAME')
RAVEN_CLIENT_ID = env('RAVEN_CLIENT_ID')
RAVEN_CLIENT_SECRET = env('RAVEN_CLIENT_SECRET')
APP_ID = env('APP_ID')
