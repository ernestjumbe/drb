"""Settings for Production Server"""
from detrundebord.settings.base import *

DEBUG = False
TEMPLATE_DEBUG = False

ADMINS = (
    ('Ernest', 'e2jeyy@gmail.com'),
)

MANAGERS = ADMINS

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
]

VAR_ROOT = '/var/www/drb'
MEDIA_ROOT = os.path.join(VAR_ROOT, 'media')
STATIC_ROOT = os.path.join(VAR_ROOT, 'static')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'detrundebord',
        'USER': 'detrundebord',
        'PASSWORD': 'detrundebord123',
        'HOST': 'localhost',
    }
}

INSTALLED_APPS += (
    #'gunicorn',
)

PREPEND_WWW = True

WSGI_APPLICATION = 'detrundebord.wsgi.application'

LOGGING = {
    'version': 1,
}

DEFAULT_FROM_EMAIL = 'no-reply@foopla.dk'

EMAIL_USE_TLS = True  
EMAIL_HOST = 'smtp.crystone.se' 
EMAIL_HOST_USER = 'no-reply@foopla.dk'  # this is my email address, use yours
EMAIL_HOST_PASSWORD = 'community123'   # set environ yourself
EMAIL_PORT = 587