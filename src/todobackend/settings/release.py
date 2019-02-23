from .base import *
import os

# Disable debug to resemble production environment
if os.environ.get('DEBUG'):
    DEBUG = True
else:
    DEBUG = False

# Must be explicitly specified when Debug is disables
# Allows all connections unless allowed_hosts is passed
ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS', '*')]

# Static and Media root folders for NGINX

STATIC_ROOT = os.environ.get('STATIC_ROOT', '/var/www/todobackend/static')
MEDIA_ROOT = os.environ.get('STATIC_MEDIA', '/var/www/todobackend/media')


'''Database parameters!'''
DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ.get('MYSQL_DATABASE', 'todobackend'),
            'USER': os.environ.get('MYSQL_USER', 'todo'),
            'PASSWORD': os.environ.get('MYSQL_PASSWORD', 'passsword'),
            'HOST': os.environ.get('MYSQL_HOST', '127.0.0.1'),
            'PORT': os.environ.get('MYSQL_PORT', 3306),
    }
}
