import unittest
import django.test

#import setups as tests_setups

from .setups import (UserFactory, SocialUserFactory, RobrechtSocialUserFactory,
                     GargantuanChallengeFactory)

from ..allauth_utils import create_allauth_user, generate_password

class SocialAccountTestCase(django.test.TestCase):
    """

    How to set up social acc for testing:
    Check in shell how a created social account user
    looks like and just recreate that.
    """

    def setUp(self):
        gf = GargantuanChallengeFactory()
        #import pdb; pdb.set_trace()
        pass

    def test_name(self):
        pass
