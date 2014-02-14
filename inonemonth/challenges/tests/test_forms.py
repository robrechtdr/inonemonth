import unittest
import django.test
from django.core.exceptions import ValidationError

from core.tests.setups import RobrechtSocialUserFactory
from ..validators import RepoExistanceValidator


###############################################################################
#                                    Forms                                    #
###############################################################################

'''
from ..forms import InvestmentModelForm

class InvestmentModelFormTestCase(TestCase):
    """
    Tests for InvestmentModelForm
    """
    def test_initial_value_of_investor_type(self):
        """
        Verify initial value of investor_type field of InvestmentModelForm.
        """
        investor_type_initial = InvestmentModelForm().fields["investor_type"].initial
        self.assertEqual(investor_type_initial, "PERSON")
'''


###############################################################################
#                                 Validators                                  #
###############################################################################

class RepoExistanceValidatorTestCase(django.test.TestCase):
    def test_name(self):
        user_rob = RobrechtSocialUserFactory()
        self.assertRaises(ValidationError, RepoExistanceValidator(user_rob), "asiakas/non_existing_branch")
