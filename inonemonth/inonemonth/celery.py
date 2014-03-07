from __future__ import absolute_import

import os

from celery import Celery
from django.conf import settings

from .settings.base import get_env_setting

# The settings must be loaded into the worker!
# (Has to use the correct db settings etc. in case your
# tasks performs a db query)
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      '{0}'.format(get_env_setting('DJANGO_SETTINGS_MODULE')))

app = Celery('inonemonth')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
