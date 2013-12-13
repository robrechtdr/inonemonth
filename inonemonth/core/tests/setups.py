import datetime
import factory
import factory.fuzzy
import random

from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model


class UserFactory(factory.DjangoModelFactory):
    """
    User factory

    User fields:
        id, password, last_login, is_superuser, username, first_name,
        last_name, email, is_staff, is_active, date_joined
    """
    FACTORY_FOR = get_user_model()
    email =  factory.Sequence(lambda n: "john.doe{0}@gmail.com".format(n))
    password = make_password("password")

    @factory.lazy_attribute
    def username(self):
        """
        Make username from email address

        Pseudo code:
        >>> self.email
        "john.doe@gmail.com"
        >>> username(self)
        "johndoe"
        """
        local_part = self.email.split("@")[0]
        return "".join(local_part.split("."))


class JimUserFactory(UserFactory):
    email = "jim.klutz@gmail.com"


class JamesUserFactory(UserFactory):
    email = "james.narcis@gmail.com"
