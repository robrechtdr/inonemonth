from __future__ import absolute_import

import unittest

import django.test

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from core.tests.setups import (RobrechtSocialUserFactory,
                               UserFactory)
from ..forms import ChallengeCreateModelForm
from ..validators import RepoExistanceValidator


User = get_user_model()


###############################################################################
#                                    Forms                                    #
###############################################################################
class ChallengeCreateModelFormTestCase(django.test.TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.form = ChallengeCreateModelForm(self.user)

    def test_body_placeholder(self):
        self.assertEqual(self.form.fields["body"].widget.attrs["placeholder"],
                         "Complete description of my challenge")

    def test_repo_placeholder(self):
        self.assertEqual(
            self.form.fields["repo"].widget.attrs["placeholder"],
            "my_repo/my_branch (existing repo on my Github account)")

    def test_title_placeholder(self):
        self.assertEqual(self.form.fields["title"].widget.attrs["placeholder"],
                         "A one line description of my challenge")


###############################################################################
#                                 Validators                                  #
###############################################################################
# Test takes about ~0.7 secs because of requests call
@unittest.skip("")
class RepoExistanceValidatorTestCase(django.test.TestCase):
    def test_repo_existance_validator(self):
        user_rob = RobrechtSocialUserFactory()
        self.assertRaises(ValidationError,
                          RepoExistanceValidator(user_rob),
                          "asiakas/non_existing_branch")
