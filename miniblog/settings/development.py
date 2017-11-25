import logging.config
import sys
from os import makedirs

from utils.loggers import record_factory
from .base import *  # NOQA

# import uwsgi
# from uwsgidecorators import timer
# from django.utils import autoreload
#
#
# @timer(3)
# def change_code_gracefull_reload(sig):
#     if autoreload.code_changed():
#         uwsgi.reload()

local = True if env('LOCAL') == 'True' else False
if 'test' not in sys.argv and local:
    DEFAULT_DATABASE_ENV = 'LOCAL_DATABASE_URL'

elif 'test' in sys.argv:
    DEFAULT_DATABASE_ENV = 'TEST_DATABASE_URL'
else:
    DEFAULT_DATABASE_ENV = 'DATABASE_URL'

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in
    # os.environ
    'default': env.db(var=DEFAULT_DATABASE_ENV),
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if env('DEBUG') == 'True' else False
TEMPLATES[0]['OPTIONS'].update({'debug': DEBUG})
TEMPLATES[0].update({"APP_DIRS": True if env('APP_DIR') == 'True' else False})

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
            'handlers': ['django', 'console'],
            'propagate': True,
            'level': 'DEBUG'
        },
        # 'django': {
        #     'handlers': ['django', 'console'],
        #     'propagate': True,
        #     'level': 'DEBUG'
        # },
    }
}

logging.config.dictConfig(LOGGING)
