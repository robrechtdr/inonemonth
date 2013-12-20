from .base import *


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
########## END IN-MEMORY TEST DATABASE CONFIGURATION
