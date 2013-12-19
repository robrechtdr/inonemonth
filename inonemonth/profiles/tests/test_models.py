import django.test

from django.contrib.auth import get_user_model

from core.tests.setups import UserFactory, JimUserFactory
from ..models import Profile
#import core.tests.setups as tests_setups

class ProfileTestCase(django.test.TestCase):
    """
    Profile TestCase

    This test should run after running profile tests. Otherwise some user tests redundant.
    """

    def setUp(self):
        pass

    @classmethod
    def setUpClass(cls):
        JimUserFactory()

    def test_profile_parameters_non_required_for_instantiation(self):
        """
        Verify if creating a base profile without passing field values
        exept for user doesn't cause an Exception.
        """
        raised = False
        user_jim = get_user_model().objects.get(email="jim.klutz@gmail.com")
        try:
            # If this causes an error, fail test.
            Profile.objects.create(user=user_jim)
        except:
            raised = True
        self.assertFalse(raised)
