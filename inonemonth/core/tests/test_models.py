import unittest
import django.test

#import setups as tests_setups

from .setups import UserFactory#, SocialUserFactory, RobrechtSocialUserFactory,
                     #GargantuanChallengeFactory)

from ..allauth_utils import create_allauth_user, generate_password

class SocialAccountTestCase(django.test.TestCase):
    """

    How to set up social acc for testing:
    Check in shell how a created social account user
    looks like and just recreate that.
    """

    def setUp(self):
        pass

    def test_name(self):
        from allauth.socialaccount.models import SocialAccount
        from allauth.socialaccount import providers


        #uf = UserFactory()
        #ufa = RobrechtSocialUserFactory()
        #gf = GargantuanChallengeFactory()
        #import pdb; pdb.set_trace()
        # extra_data is extracted with
        # LinkedInOAuth2Adapter.get_user_token(token)
        extra_data = {u'avatar_url': u'https://gravatar.com/avatar/a13f182fbfe06570501700a310b5cf45?d=https%3A%2F%2Fidenticons.github.com%2F14e49a04ed384e716fcd708995faa62b.png&r=x',
                      u'bio': None,
                      u'blog': None,
                      u'company': None,
                      u'created_at': u'2012-08-15T10:56:03Z',
                      u'email': u'robrecht.de.rouck at gmail dot com',
                      u'events_url': u'https://api.github.com/users/RobrechtDR/events{/privacy}',
                      u'followers': 0,
                      u'followers_url': u'https://api.github.com/users/RobrechtDR/followers',
                      u'following': 0,
                      u'following_url': u'https://api.github.com/users/RobrechtDR/following{/other_user}',
                      u'gists_url': u'https://api.github.com/users/RobrechtDR/gists{/gist_id}',
                      u'gravatar_id': u'a13f182fbfe06570501700a310b5cf45',
                      u'hireable': False,
                      u'html_url': u'https://github.com/RobrechtDR',
                      u'id': 2156349,
                      u'location': u'Belgium',
                      u'login': u'RobrechtDR',
                      u'name': u'Robrecht De Rouck',
                      u'organizations_url': u'https://api.github.com/users/RobrechtDR/orgs',
                      u'public_gists': 1,
                      u'public_repos': 10,
                      u'received_events_url': u'https://api.github.com/users/RobrechtDR/received_events',
                      u'repos_url': u'https://api.github.com/users/RobrechtDR/repos',
                      u'site_admin': False,
                      u'starred_url': u'https://api.github.com/users/RobrechtDR/starred{/owner}{/repo}',
                      u'subscriptions_url': u'https://api.github.com/users/RobrechtDR/subscriptions',
                      u'type': u'User',
                      u'updated_at': u'2014-01-29T22:27:37Z',
                      u'url': u'https://api.github.com/users/RobrechtDR'}
        user = create_allauth_user(email="de.rouck.robrecht@gmail.com",
                                   password="my_password")
        from allauth.account.models import EmailAddress
        from django.contrib.auth import get_user_model
        User = get_user_model()
        """
        kuser = User.objects.create(password="my_password", email="
        email_address = EmailAddress.objects.create(user=kuser,
                                                    email="robrecht5000@hotmail.com)
        import pdb; pdb.set_trace()
        """
        social_acc = SocialAccount.objects.create(
            user=user,
            provider=u"github",
            # http://caius.github.io/github_id/#Lukasa
            uid=u"1382556",
            extra_data=extra_data
        )

