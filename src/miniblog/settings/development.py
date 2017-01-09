import logging.config
import sys
from os import makedirs

from utils.loggers import record_factory
from .base import *  # NOQA

DATABASES = {
    'default': {
        'ENGINE': env('ENGINE'),
        'NAME': "miniblog",
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST')
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATES[0]['OPTIONS'].update({'debug': DEBUG})
TEMPLATES[0].update({"APP_DIRS": DEBUG})

# Turn off debug while imported by Celery with a workaround
# See http://stackoverflow.com/a/4806384
if "celery" in sys.argv[0]:
    DEBUG = False

# Django Debug Toolbar
INSTALLED_APPS += (
    'debug_toolbar.apps.DebugToolbarConfig',)

# Show emails MIDDLEWARE_CLASSES
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

# to console in DEBUG mode

# Show thumbnail generation errors
THUMBNAIL_DEBUG = DEBUG

# Log everything to the logs directory at the top
logfile_path = env('LOG_FILE_PATH')
makedirs(logfile_path, exist_ok=True)
LOGFILE_ROOT = join(BASE_DIR, logfile_path)

# Reset logging
# (see http://www.caktusgroup.com/blog/2015/01/27/Django-Logging-Configuration-logging_config-default-settings-logger/)

LOGGING_CONFIG = None
logging.setLogRecordFactory(record_factory)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] [%(ip)s %(host)s] [%(project)s] %(levelname)s "
                      "[%(name)s] [%(pathname)s:%(lineno)s-%(funcName)s()] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'django': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024 * 1024 * 100,
            'backupCount': 10,
            'filename': join(LOGFILE_ROOT, 'django.log'),
            'formatter': 'verbose'
        },
        'blog': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': join(LOGFILE_ROOT, 'blog.log'),
            'formatter': 'verbose'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'werkzeug': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'blog': {
            'handlers': ['blog'],
            'level': 'DEBUG',
            'propagate': True

        },
        'django.request': {
            'handlers': ['django'],
            'propagate': True,
            'level': 'DEBUG'
        },
    }
}

logging.config.dictConfig(LOGGING)

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
CRISPY_TEMPLATE_PACK = 'bootstrap3'
