import unittest
import django.test

import core.tests.setups as tests_setups

from django.contrib.auth import get_user_model
from django.db.models.fields import FieldDoesNotExist


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
        pass

    def test_first_name_attribute_is_removed(self):
        """
        Verify if the first_name attribute of the customized User is removed.
        """
        # Alternative: (bit slower)
        #user_field_classes = get_user_model()._meta.local_fields
        #user_fields = [field.name for field in user_field_classes]
        #self.assertTrue("first_name" not in user_fields)
        self.assertRaises(FieldDoesNotExist, get_user_model()._meta.get_field, "first_name")


    def test_last_name_attribute_is_removed(self):
        """
        Verify if the last_name attribute of the customized User is removed.
        """
        self.assertRaises(FieldDoesNotExist, get_user_model()._meta.get_field, "last_name")


    def test_user_parameters_non_required_for_instantiation(self):
        """
        Verify if creating a custom user without passing field values
        causes an Exception.
        """
        user_model = get_user_model()
        raised = False
        try:
            # If this causes an error, fail test.
            user_model.objects.create()
        except:
            raised = True
        self.assertFalse(raised)
