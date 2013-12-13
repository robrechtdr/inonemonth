from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile

class BaseProfile(UserenaBaseProfile):
    user = models.OneToOneField(get_user_model(), unique=True, verbose_name=_('user'))
