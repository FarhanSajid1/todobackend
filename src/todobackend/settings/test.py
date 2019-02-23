from .base import *
import os

#installing apps
INSTALLED_APPS += ('django_nose', )
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
TEST_OUTPUT_DIR = os.environ.get('TEST_OUTPUT_DIR', '.') # that variable or in pwd
NOSE_ARGS = [
    '--verbosity=2',
    '--nologcapture',
    '--with-coverage',
    '--cover-package=todo',
    '--with-spec',
    '--with-xunit',
    f'--xunit-file={TEST_OUTPUT_DIR}/unittests.xml',
    '--cover-xml',
    f'--cover-xml-file={TEST_OUTPUT_DIR}/coverage.xml'



]
'''Database parameters!'''
DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ.get('MYSQL_DATABASE', 'todobackend'),
            'USER': os.environ.get('MYSQL_USER', 'todo'),
            'PASSWORD': os.environ.get('MYSQL_PASSWORD', 'passsword'),
            'HOST': os.environ.get('MYSQL_HOST', '127.0.0.1'),
            'PORT': os.environ.get('MYSQL_PORT', 3306)
    }
}