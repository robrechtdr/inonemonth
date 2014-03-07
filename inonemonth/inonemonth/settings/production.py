"""Production settings and globals."""

from __future__ import absolute_import

import dj_database_url

from .base import *


########## HOST CONFIGURATION
# See: https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = []
########## END HOST CONFIGURATION


########## HEROKU CONFIGURATION
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']
########## END HEROKU CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
          'default': {
                      'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
                     }
         }
########## END CACHE CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = get_env_setting('SECRET_KEY')
########## END SECRET CONFIGURATION


########## STATIC FILES CONFIGURATION
# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html
AWS_STORAGE_BUCKET_NAME = 'inonemonth'

# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html
STATIC_URL = 'https://s3-eu-west-1.amazonaws.com/{0}/'.format(
    AWS_STORAGE_BUCKET_NAME)

# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html
AWS_ACCESS_KEY_ID = get_env_setting('AWS_ACCESS_KEY_ID')

# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html
AWS_SECRET_ACCESS_KEY = get_env_setting('AWS_SECRET_ACCESS_KEY')

# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html
STATICFILES_STORAGE = DEFAULT_FILE_STORAGE
########## END STATIC FILES CONFIGURATION


########## MIDDLEWARE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
# Prepend ssl middleware
MIDDLEWARE_CLASSES = (
    'sslify.middleware.SSLifyMiddleware',
) + MIDDLEWARE_CLASSES
########## END MIDDLEWARE CONFIGURATION


########## SECURE COOKIES CONFIGURATION
# Not in local because Django dev server doesn't readily support https:
# http://stackoverflow.com/questions/7610394/
# how-to-setup-ssl-on-a-local-django-server-to-test-a-facebook-app

# See: https://docs.djangoproject.com/en/dev/topics/security/#ssl-https
SESSION_COOKIE_SECURE = True

# See: https://docs.djangoproject.com/en/dev/topics/security/#ssl-https
CSRF_COOKIE_SECURE = True
########## END SECURE COOKIES CONFIGURATION


########## GUNICORN CONFIGURATION
# See:
INSTALLED_APPS += (
    'gunicorn',
)
########## END GUNICORN CONFIGURATION


########## STORAGES CONFIGURATION
# See:
INSTALLED_APPS += (
    'storages',
)
########## END STORAGES CONFIGURATION


########## ALLAUTH CONFIGURATION
# See: http://django-allauth.readthedocs.org/en/latest/#github
ALLAUTH_SOCIAL_APP_GITHUB_ID = "d620d1cebf6f5ed095b4"
########## END ALLAUTH CONFIGURATION


########## CELERY CONFIGURATION
# http://docs.celeryproject.org/en/latest/configuration.html#example-configuration-file
BROKER_URL = get_env_setting("CLOUDAMQP_URL")
########## END CELERY CONFIGURATION
