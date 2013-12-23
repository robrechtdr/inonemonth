import django.test

from django.contrib.auth import get_user_model

from core.tests.setups import ProfilePseudoFactory, JimUserFactory, UserFactory

from ..models import Profile


class ProfileTestCase(django.test.TestCase):
    """
    Profile TestCase
    """

    @classmethod
    def setUpClass(cls):
        pass

    def test_get_profile(self):
        """
        Verify if getting a profile works.
        """
        raised = False
        try:
            # If this causes an error, fail test.
            ProfilePseudoFactory()
            Profile.objects.all()[0]
        except:
            raised = True

        self.assertFalse(raised)
