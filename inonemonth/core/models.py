from __future__ import absolute_import

from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


# Not convienient to implement a custom user model
# a.t.m. with allauth.
class UserExtension(models.Model):
    user = models.OneToOneField(User)
    temp_password = models.CharField(max_length=8)
