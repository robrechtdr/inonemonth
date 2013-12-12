import unittest
import django.test
from django.contrib.auth import get_user_model

import core.tests.setups as tests_setups

#from userena.tests.profiles.test import ProfileTestCase
#from userena.models import UserenaSignup

#from apps.profiles.models import InvestorProfile, InvestorEntity
#from apps.startups.models import Company

#from ..models import Investment

class InonemonthUserTestCase(unittest.TestCase):
    """
    Tests for InonemonthUser model.

    With Postgresql backend:
    Run with django.test.TestCase: 9.4 secs
    Run with unittest.TestCase: 9.4 secs

    With SQLite backend:
    Run with unittest.TestCase: 0.5 secs

    """
    def setUp(self):
        """
        Set up.
        """
        #investor_profile = test_setups.get_investor_profile()
        #tests_setups.InvestmentFactory(investor_profile=investor_profile)
        pass

    def test_first_name_attribute_is_removed(self):
        """
        Verify if the first_name attribute of the customized User is removed.
        """
        user_field_classes = get_user_model()._meta.local_fields
        user_fields = [field.name for field in user_field_classes]
        #self.assertNotIn(hasattr(user_model, "first_name"))
        self.assertTrue("first_name" not in user_fields)


    def test_last_name_attribute_is_removed(self):
        """
        Verify if the last_name attribute of the customized User is removed.
        """
        user_field_classes = get_user_model()._meta.local_fields
        user_fields = [field.name for field in user_field_classes]
        self.assertTrue("last_name" not in user_fields)






'''
class InvestmentTestCase(TestCase):
    """
    Tests for Investment model.
    """
    def setUp(self):
        """
        Set up.
        """
        investor_profile = test_setups.get_investor_profile()
        tests_setups.InvestmentFactory(investor_profile=investor_profile)

    def test_if_not_both_investor_types_simultaneously_set(self):
        """
        Verify if either investor_profile or investor_entity value is set and not both at the same time.

        I will need to make 2 factories for that (use inhertance),
        one that sets only profiles and one that sets only entities.
        """
        pass

    def test_investor_identity_attribute(self):
        """
        Verify investory identity attribute.
        """
        investment = Investment.objects.get(pk=1)
        # blablabla
        pass

    def test_unicode_attribute(self):
        """
        Verify unicode attribute.

        Relies on previous tests. If they work this should work.
        """
        pass
'''
