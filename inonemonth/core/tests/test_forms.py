from django.test import TestCase
from ..forms import InonemonthAuthenticationForm
#from core.forms import InonemonthAuthenticationForm


class InonemonthAuthenticationFormTestCase(TestCase):
    def test_form_has_placeholder_and_css_class(self):
        form = InonemonthAuthenticationForm()
        self.assertIn("placeholder", form.as_p())
        #self.assertIn("placeholder", form.fields["identification"].widget.attrs)
        self.assertIn("class", form.as_p())

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
