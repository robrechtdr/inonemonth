"""Common settings and globals."""

from __future__ import absolute_import

from os import environ
from os.path import abspath, basename, dirname, join, normpath
from sys import path
from dateutil.relativedelta import relativedelta

# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured


def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)


########## PATH CONFIGURATION
# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(DJANGO_ROOT)

# Site name:
SITE_NAME = basename(DJANGO_ROOT)

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(DJANGO_ROOT)
########## END PATH CONFIGURATION


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
('Robrecht', 'de.rouck.robrecht@gmail.com'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
########## END MANAGER CONFIGURATION


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'inonemonth',
        'USER': environ.get('DBUSER', "my_username"),
        'PASSWORD': environ.get('DBPASSWORD', 'my_password'),
        'HOST': '',
        'PORT': '',
    }
}
########## END DATABASE CONFIGURATION


########## GENERAL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = 'Europe/London'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
# To avoid deleting the example.com entry for each db setup
SITE_ID = 2

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
########## END GENERAL CONFIGURATION


########## MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'
########## END MEDIA CONFIGURATION


########## STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = normpath(join(SITE_ROOT, 'assets'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
normpath(join(SITE_ROOT, 'static')),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
'django.contrib.staticfiles.finders.FileSystemFinder',
'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
########## END STATIC FILE CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key should only be used for development and testing.
SECRET_KEY = r"^!!8(e%nbjoauefzo9jszx@o*fa#7r7jt%9p9ec6j^0qut6m&!"
########## END SECRET CONFIGURATION


########## SITE CONFIGURATION
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []
########## END SITE CONFIGURATION


########## FIXTURE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
normpath(join(SITE_ROOT, 'fixtures')),
)
########## END FIXTURE CONFIGURATION


########## TEMPLATE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
TEMPLATE_CONTEXT_PROCESSORS = (
'django.contrib.auth.context_processors.auth',
'django.core.context_processors.debug',
'django.core.context_processors.i18n',
'django.core.context_processors.media',
'django.core.context_processors.static',
'django.core.context_processors.tz',
'django.contrib.messages.context_processors.messages',
'django.core.context_processors.request',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
TEMPLATE_LOADERS = (
'django.template.loaders.filesystem.Loader',
'django.template.loaders.app_directories.Loader',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
TEMPLATE_DIRS = (
normpath(join(SITE_ROOT, 'templates')),
)
########## END TEMPLATE CONFIGURATION


########## MIDDLEWARE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
MIDDLEWARE_CLASSES = (
# Default Django middleware.
'django.middleware.common.CommonMiddleware',
'django.contrib.sessions.middleware.SessionMiddleware',
'django.middleware.csrf.CsrfViewMiddleware',
'django.contrib.auth.middleware.AuthenticationMiddleware',
'django.contrib.messages.middleware.MessageMiddleware',
'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
########## END MIDDLEWARE CONFIGURATION


########## URL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = '%s.urls' % SITE_NAME
########## END URL CONFIGURATION


########## APP CONFIGURATION
DJANGO_APPS = (
# Default Django apps:
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.sites',
'django.contrib.messages',
'django.contrib.staticfiles',

# Useful template tags:
# 'django.contrib.humanize',

# Admin panel and documentation:
'django.contrib.admin',
# 'django.contrib.admindocs',
)

# Apps specific for this project go here.
LOCAL_APPS = (
'core',
'challenges',
'comments',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS
########## END APP CONFIGURATION


########## LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
'version': 1,
'disable_existing_loggers': False,
'filters': {
    'require_debug_false': {
        '()': 'django.utils.log.RequireDebugFalse'
    }
},
'handlers': {
    'mail_admins': {
        'level': 'ERROR',
        'filters': ['require_debug_false'],
        'class': 'django.utils.log.AdminEmailHandler'
    }
},
'loggers': {
    'django.request': {
        'handlers': ['mail_admins'],
        'level': 'ERROR',
        'propagate': True,
    },
}
}
########## END LOGGING CONFIGURATION


########## WSGI CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = '%s.wsgi.application' % SITE_NAME
########## END WSGI CONFIGURATION


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = 'smtp.gmail.com'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD', '')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER', 'your_email@example.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = 587

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = EMAIL_HOST_USER
########## END EMAIL CONFIGURATION


########## AUTHENTICATION BACKENDS CONFIGURATION
# See: https://docs.djangoproject.com/en/1.5/ref/settings/#std:setting-AUTHENTICATION_BACKENDS
AUTHENTICATION_BACKENDS = (
'django.contrib.auth.backends.ModelBackend',
)
########## END AUTHENTICATION BACKENDS CONFIGURATION


########## INONEMONTH CONFIGURATION
CHALLENGE_PERIOD_DURATION = relativedelta(months=1)
VOTING_PERIOD_DURATION = relativedelta(weeks=1)
########## END INONEMONTH CONFIGURATION


########## CRISPY FORMS CONFIGURATION
INSTALLED_APPS += (
'crispy_forms',
)
CRISPY_TEMPLATE_PACK = 'bootstrap3'
########## END CRISPY FORMS CONFIGURATION


########## SOUTH CONFIGURATION
INSTALLED_APPS += (
'south',
)
########## END SOUTH CONFIGURATION


########## PAGEDOWN CONFIGURATION
INSTALLED_APPS += (
'pagedown',
)
########## END PAGEDOWN CONFIGURATION


########## MARKDOWN-DEUX CONFIGURATION
# https://github.com/trentm/django-markdown-deux#django-project-setup
INSTALLED_APPS += (
'markdown_deux',
)
########## END MARKDOWN-DEUX CONFIGURATION


########## ALLAUTH CONFIGURATION
TEMPLATE_CONTEXT_PROCESSORS += (
    # Required by allauth template tags
    "django.core.context_processors.request",

    # allauth specific context processors
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)

AUTHENTICATION_BACKENDS += (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

INSTALLED_APPS += (
    # The Django sites framework is required
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.github',
)

##### Implement email as main user field and remove username
# See: http://stackoverflow.com/questions/19683179/remove-username-field-from-django-allauth
# Specifies the login method to use -- whether the
# user logs in by entering his username, e-mail address, or either one of both.
ACCOUNT_AUTHENTICATION_METHOD = "email" #("email",)

# Allauth fails if this is not set to true and
# ACCOUNT_AUTHENTICATION_METHOD is set to "email"
# See allauth/account/app_settings ln 20.
ACCOUNT_EMAIL_REQUIRED = True

# To get rid of username field
ACCOUNT_USERNAME_REQUIRED = False
##### end

# http://django-allauth.readthedocs.org/en/latest/#github
ALLAUTH_SOCIAL_APP_GITHUB_SECRET = get_env_setting('ALLAUTH_SOCIAL_APP_GITHUB_SECRET')

# http://django-allauth.readthedocs.org/en/latest/#configuration
# Since a user can only sign up via Github and only jurors
# will have accounts that are not linked to github, it is
# not necessary or even sensical to let them verify their
# accounts. They start their access through the site via
# an invite email anyway.
ACCOUNT_EMAIL_VERIFICATION = "none"

# Otherwise someone could create a challenge with someone
# else's email address and send this out to employers,
# potentially placing him/her in an embarressing situation.
SOCIALACCOUNT_EMAIL_VERIFICATION = "mandatory" #"none"

LOGIN_URL = "/challenge/create/"
LOGIN_REDIRECT_URL = LOGIN_URL
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = LOGIN_URL

# Doesn't seem to work for Github:
# https://github.com/pennersr/django-allauth/issues/369
#SOCIALACCOUNT_QUERY_EMAIL = True
########## end ALLAUTH CONFIGURATION


########## RESTFRAMEWORK CONFIGURATION
INSTALLED_APPS += (
'rest_framework',
)
########## END RESTFRAMEWORK CONFIGURATION


########## CELERY CONFIGURATION
# https://github.com/celery/celery/tree/master/examples/django
# http://docs.celeryproject.org/en/latest/configuration.html#example-configuration-file
BROKER_URL = 'amqp://localhost:5672//'
BROKER_POOL_LIMIT = 3
########## END CELERY CONFIGURATION
