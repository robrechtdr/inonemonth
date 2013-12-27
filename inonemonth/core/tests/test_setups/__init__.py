import django.test
import unittest

from profiles.models import Profile

from ..setups import ProfilePseudoFactory, ProfilePseudoFactory, UserFactory
from .utils import get_only_fields_defined_in_child_model


class UserFactoryTestCase(django.test.TestCase):
    """Test UserFactoryTestCase for similarities with a regular factory"""

    def test_instantiation(self):
        """
        Verify that simple instantiation doesn't fail.
        """

        raised = False
        try:
            # If this causes an error, fail test.
            user = UserFactory()
        except:
            raised = True

        self.assertFalse(raised)

        # Only objects saved to the database have a pk method that is not None
        self.assertNotEqual(user.pk, None)


class ProfilePseudoFactoryTestCase(django.test.TestCase):
    """
    Test ProfilePseudoFactoryTestCase for similarities with a regular factory.
    """
    def test_profile_gets_additional_field(self):
        """
        Test if Profile gets additional fields and
        warn to update ProfilePseudoFactory.
        """
        self.assertEqual(get_only_fields_defined_in_child_model(Profile),
                         [u"id", "user"],
                         msg="Adapt ProfilePseudoFactory to test for new field of Profile!")

    def test_instantiation(self):
        """
        Verify that some characteristics are similar to those of a
        regular factory.
        """
        profile_pseudo_factory = ProfilePseudoFactory()
        profile_indirect = UserFactory().profile

        self.assertEqual(profile_pseudo_factory._meta.get_all_field_names(),
                         profile_indirect._meta.get_all_field_names())

        # Only objects saved to the database have a pk method that is not None
        self.assertNotEqual(profile_pseudo_factory.pk, None)

    # Requires code changes to Userena to implement build and not necessary for
    # the moment.
    @unittest.expectedFailure
    def test_build_method(self):
        """
        Verify that some characteristics of build are similar to those of a
        regular factory.
        """
        profile_pseudo_factory_build = ProfilePseudoFactory.build()
        profile_pseudo_factory_inst = ProfilePseudoFactory()

        self.assertEqual(type(profile_pseudo_factory_build),
                         type(profile_pseudo_factory_inst))
        self.assertEqual(profile_pseudo_factory_build._meta.get_all_field_names(),
                         profile_pseudo_factory_inst._meta.get_all_field_names())
        self.assertNotEqual(profile_pseudo_factory_build.pk, None)

    def test_create_batch_method(self):
        """
        Verify that some characteristics of create_batch are similar
        to those of a regular factory.
        """
        self.assertEqual(type(ProfilePseudoFactory.create_batch(3)[2]),
                         type([i.profile for i in UserFactory.create_batch(3)][2]))
