from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile
#import pdb; pdb.set_trace()
#from challenges.models import Challenge

class Profile(UserenaBaseProfile):
    user = models.OneToOneField(get_user_model(), unique=True, verbose_name=_('user'))


#class Lincoln(BaseProfile):
#    pass
    #challenge = models.ForeignKey(Challenge, null=True)
