from .base import *
import os
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleado',
        'USER': 'camilo',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}


STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')
