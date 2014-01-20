# Create your views here.


'''
from allauth.socialaccount.models import SocialLogin, SocialAccount
from django.contrib.auth import get_user_model

social_acc = get_user_model().objects.all()[1].socialaccount_set.all()[0]
#<SocialAccount: de.rouck.robrecht>
social_acc.extra_data["url"]
#u"https://api.gthub.com/users/RobrechtDR"
social_acc.extra_data["name"]
#"Robrecht De Rouck"

# or

SocialAccount.objects.all()
#[<SocialAccount: de.rouck.robrecht>]

'''
