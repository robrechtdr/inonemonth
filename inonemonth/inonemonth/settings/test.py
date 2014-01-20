from .base import *

# Instead of duplicating data from local, just import one by one
from .local import ALLAUTH_SOCIAL_APP_GITHUB_ID

# For functional tests
########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
#DEBUG = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
#TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION
#ALLOWED_HOSTS = ['127.0.0.1']

########## IN-MEMORY TEST DATABASE CONFIGURATION
# Time diff for 1 testcase, with PostgreSQL 9.4 secs, SQLite 0.5 secs.
# However, run tests in local(with PostgreSQL) at least before merging into
# production to test for RDBMS specific results.
# See: http://www.celerity.com/blog/2013/04/29/how-write-speedy-unit-tests-django-part-1-basics/
#      https://docs.djangoproject.com/en/dev/ref/settings/#databases
#      https://www.sqlite.org/inmemorydb.html
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/home/robrecht/src/my_projects/inonemonth/inonemonth/test.db',
    }
}
'''
########## END IN-MEMORY TEST DATABASE CONFIGURATION


########## LETTUCE CONFIGURATION
# See: http://lettuce.it/recipes/django-lxml.html#lettuce-install-the-lettuce-django-app
INSTALLED_APPS += (
    'lettuce.django',
)
########## END LETTUCE CONFIGURATION
