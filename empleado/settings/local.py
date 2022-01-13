from .base import *
import os
import django_heroku
# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True
ALLOWED_HOSTS = ['empleado.herokuapp.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dbohpkkp3o0mio',
        'USER': 'xspiyyehkklogz',
        'PASSWORD': '8505bebf6705dc72dc5fc100ca826c24a86ea2047d874161b1683835266fa22c',
        'HOST': 'ec2-54-198-213-75.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = 'static/'
django_heroku.settings(locals())
STATICFILES_DIRS = [BASE_DIR.child('static')]
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')
