from __future__ import absolute_import

from .production import *


########## STATIC FILES CONFIGURATION
# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html
AWS_STORAGE_BUCKET_NAME = 'inonemonth'

# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html
STATIC_URL = 'https://s3-eu-west-1.amazonaws.com/{0}/'.format(AWS_STORAGE_BUCKET_NAME)

# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html
AWS_ACCESS_KEY_ID = get_env_setting('AWS_ACCESS_KEY_ID')

# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html
AWS_SECRET_ACCESS_KEY = get_env_setting('AWS_SECRET_ACCESS_KEY')

# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html
STATICFILES_STORAGE = DEFAULT_FILE_STORAGE
########## END STATIC FILES CONFIGURATION


########## ALLAUTH CONFIGURATION
# See: http://django-allauth.readthedocs.org/en/latest/#github
ALLAUTH_SOCIAL_APP_GITHUB_ID = "189e9b562c8b67cb17bb"
########## END ALLAUTH CONFIGURATION
