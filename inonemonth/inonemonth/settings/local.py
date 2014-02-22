"""Development settings and globals."""

from __future__ import absolute_import

from os.path import join, normpath

from .base import *


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
'''
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
'''
########## END CACHE CONFIGURATION


########## INONEMONTH CONFIGURATION
#CHALLENGE_PERIOD_DURATION = relativedelta(months=1)
CHALLENGE_PERIOD_DURATION = relativedelta(months=0)
VOTING_PERIOD_DURATION = relativedelta(weeks=1)
########## END INONEMONTH CONFIGURATION


########## TOOLBAR CONFIGURATION
# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INSTALLED_APPS += (
    'debug_toolbar',
)

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INTERNAL_IPS = ('127.0.0.1',)

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TEMPLATE_CONTEXT': True,
}
########## END TOOLBAR CONFIGURATION


########## ALLAUTH CONFIGURATION
# See: http://django-allauth.readthedocs.org/en/latest/#github
ALLAUTH_SOCIAL_APP_GITHUB_ID = "9a99010075a295b4855a"
########## END ALLAUTH CONFIGURATION


########## LETTUCE CONFIGURATION
# See: http://lettuce.it/recipes/django-lxml.html#lettuce-install-the-lettuce-django-app
INSTALLED_APPS += (
    'lettuce.django',
)
########## END LETTUCE CONFIGURATION
