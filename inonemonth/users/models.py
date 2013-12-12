from django.db import models
from authtools.models import AbstractEmailUser, UserManager

class User(AbstractEmailUser):
    """
    A customized User class

    Fields: id, email, password, last_login, is_superuser, is_staff,
    is_active and date_joined.
    """
    pass
