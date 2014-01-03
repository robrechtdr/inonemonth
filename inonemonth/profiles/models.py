from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile


class Profile(UserenaBaseProfile):
    """
    Userena Profile model

    There seems to be no easy way to create a profile directly
    with a Django userena Profile.

    To Create a user with automatically generated Profile:
    > from userena.models import UserenaSignup
    > user = UserenaSignup.objects.create_user(username="my_username",
                                               email="name@gmail.com",
                                               password="my_password")
    To get a created profile
    > user.profile
    # or
    > Profile.objects.get(user=user)
    """
    user = models.OneToOneField(get_user_model(), unique=True, verbose_name=_('user'))
