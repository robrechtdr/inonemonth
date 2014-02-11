import django.test
import unittest

from django.core.management import call_command
from django.contrib.auth import get_user_model
from challenges.models import Challenge, Role

from core.tests.setups import (GargantuanChallengeFactory, ChallengeFactory,
                               UserFactory, JurorRoleFactory,
                               TimeFixedGargantuanChallengeFactory,
                               InVotingPeriodGargantuanChallengeFactory,
                               EndedGargantuanChallengeFactory)

User = get_user_model()


class GetRepresentationForUserTestCase(django.test.TestCase):
    def setUp(self):
        call_command('setup_allauth_social', 'github', domain="http://localhost", setting="test")
        GargantuanChallengeFactory()

    def tearDown(self):
        UserFactory.reset_sequence(1)

    def test_clencher_as_role_and_juror_as_user_role(self):
        self.assertEqual("", "Clencher (de.rouck.robrecht@gmail.com)")

    def test_juror_as_role_and_other_juror_as_user_role(self):
        self.assertEqual("", "Juror 2")

    def test_juror_as_role_and_identical_juror_as_user_role(self):
        self.assertEqual("", "Juror 1 (me)")

    # If role and user_role are clenchers, is always the same person
    # because there is only 1 clencher per challenge.
    def test_clencher_as_role_and_clencher_as_user_role(self):
        self.assertEqual("", "Clencher (me)")

    def test_juror_as_role_and_clencher_as_user_role(self):
        self.assertEqual("", "Juror 1 (andy.slacker@gmail.com)")
