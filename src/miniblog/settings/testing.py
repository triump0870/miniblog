# Setting spefically for testing environment
from .base import *				# NOQA

DEBUG = True
TEMPLATES[0]['OPTIONS'].update({'debug': True})

INSTALLED_APPS += (
    'django_nose',
    )

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=blog, api, profiles, accounts',
    '--cover-inclusive',
] 