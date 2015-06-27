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
    '46.101.255.172',
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
    'gunicorn',
    'raven.contrib.django.raven_compat',
)

RAVEN_CONFIG = {
    'dsn': 'https://9c561277d4a54378989e6bd7f860022d:7d50e2f9905d4be0a5605f1d62f8b7ad@app.getsentry.com/46863',
}

PREPEND_WWW = False

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