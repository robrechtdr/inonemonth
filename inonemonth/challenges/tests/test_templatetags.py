from __future__ import absolute_import

import django.test

from django.contrib.auth import get_user_model
from django.core.management import call_command

from core.tests.setups import (GargantuanChallengeFactory,
                               UserFactory)

from ..models import Challenge
from ..templatetags.challenges_extras import get_representation_for_user


User = get_user_model()


class GetRepresentationForUserTestCase(django.test.TestCase):
    def setUp(self):
        call_command('setup_allauth_social',
                     'github',
                     domain="http://localhost",
                     setting="test")
        GargantuanChallengeFactory()

    def tearDown(self):
        UserFactory.reset_sequence(1)

    def test_clencher_as_role_and_juror_as_user_role(self):
        challenge = Challenge.objects.get(id=1)
        role = challenge.get_clencher()

        andy = User.objects.get(email="andy.slacker@gmail.com")
        user_role = challenge.role_set.get(user=andy)
        self.assertEqual(get_representation_for_user(role, user_role),
                         "Clencher (de.rouck.robrecht@gmail.com)")

    def test_juror_as_role_and_other_juror_as_user_role(self):
        challenge = Challenge.objects.get(id=1)
        fred = User.objects.get(email="fred.labot@gmail.com")
        role = challenge.role_set.get(user=fred)

        andy = User.objects.get(email="andy.slacker@gmail.com")
        user_role = challenge.role_set.get(user=andy)
        self.assertEqual(get_representation_for_user(role, user_role),
                         "Juror 2")

    def test_juror_as_role_and_identical_juror_as_user_role(self):
        challenge = Challenge.objects.get(id=1)
        andy = User.objects.get(email="andy.slacker@gmail.com")
        role = challenge.role_set.get(user=andy)

        user_role = role
        self.assertEqual(get_representation_for_user(role, user_role),
                         "Juror 1 (me)")

    # If role and user_role are clenchers, is always the same person
    # because there is only 1 clencher per challenge.
    def test_clencher_as_role_and_clencher_as_user_role(self):
        challenge = Challenge.objects.get(id=1)
        role = challenge.get_clencher()

        robrecht = User.objects.get(email="de.rouck.robrecht@gmail.com")
        user_role = challenge.role_set.get(user=robrecht)
        self.assertEqual(get_representation_for_user(role, user_role),
                         "Clencher (me)")

    def test_juror_as_role_and_clencher_as_user_role(self):
        challenge = Challenge.objects.get(id=1)
        andy = User.objects.get(email="andy.slacker@gmail.com")
        role = challenge.role_set.get(user=andy)

        robrecht = User.objects.get(email="de.rouck.robrecht@gmail.com")
        user_role = challenge.role_set.get(user=robrecht)
        self.assertEqual(get_representation_for_user(role, user_role),
                         "Juror 1 (andy.slacker@gmail.com)")
