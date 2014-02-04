import django.test
import unittest

from django.core.management import call_command
from django.contrib.auth import get_user_model
from challenges.models import Challenge, Role

from core.tests.setups import (GargantuanChallengeFactory, ChallengeFactory,
                               UserFactory, JurorRoleFactory)


class ChallengeTestCase(django.test.TestCase):
    def setUp(self):
        call_command('setup_allauth_social', 'github', domain="http://localhost", setting="test")
        GargantuanChallengeFactory()

    def tearDown(self):
        UserFactory.reset_sequence(1)

    def test_get_unicode(self):
        challenge = Challenge.objects.get(id=1)
        self.assertEqual(challenge.__unicode__(),
                         "Challenge 1, created on Tue Feb  4 09:15:00 2014")

    def test_get_absolute_url(self):
        challenge = Challenge.objects.get(id=1)
        self.assertEqual(challenge.get_absolute_url(), "/api/challenges/1/")

    def test_get_clencher(self):
        challenge = Challenge.objects.get(id=1)
        self.assertEqual(challenge.get_clencher().user.email, u"de.rouck.robrecht@gmail.com")

    def test_get_jurors(self):
        challenge = Challenge.objects.get(id=1)
        self.assertEqual([juror.user.email for juror in challenge.get_jurors()],
                         [u'john.doe2@gmail.com', u'john.doe3@gmail.com'])

    @unittest.skip("For development periods shorter than one month will be used")
    def test_get_challenge_period_end_datetime(self):
        challenge = Challenge.objects.get(id=1)
        self.assertEqual(challenge.get_challenge_period_end_datetime().ctime(),
                         'Tue Mar  4 09:15:00 2014')

    @unittest.skip("For development periods shorter than one week will be used")
    def test_get_voting_period_end_datetime(self):
        challenge = Challenge.objects.get(id=1)
        self.assertEqual(challenge.get_challenge_period_end_datetime().ctime(),
                         'Wed Feb  5 09:15:00 2014')


class RoleTestCase(django.test.TestCase):
    def setUp(self):
        call_command('setup_allauth_social', 'github', domain="http://localhost", setting="test")
        GargantuanChallengeFactory()

    def tearDown(self):
        UserFactory.reset_sequence(1)

    def test_get_unicode(self):
        challenge = Challenge.objects.get(id=1)
        clencher = challenge.get_clencher()
        self.assertEqual(clencher.__unicode__(),
                         "Clencher 'de.rouck.robrecht' of 'Challenge 1, created on Tue Feb  4 09:15:00 2014'")

    def test_get_absolute_url(self):
        challenge = Challenge.objects.get(id=1)
        clencher = challenge.get_clencher()
        self.assertEqual(clencher.get_absolute_url(), "/api/roles/1/")

    def test_clencher_cant_vote(self):
        challenge = Challenge.objects.get(id=1)
        clencher = challenge.get_clencher()
        self.assertEqual(clencher.can_vote(), False)

    def test_juror_can_vote(self):
        challenge = Challenge.objects.get(id=1)
        juror = challenge.get_jurors()[0]
        self.assertEqual(juror.can_vote(), True)

    def test_clencher_cant_make_head_comment(self):
        challenge = Challenge.objects.get(id=1)
        clencher = challenge.get_clencher()
        self.assertEqual(clencher.can_make_head_comment(), False)

    def test_juror_without_headcomments_can_make_head_comment(self):
        challenge = Challenge.objects.get(id=1)
        juror = JurorRoleFactory() # without head comment
        self.assertEqual(juror.can_make_head_comment(), True)

    def test_juror_with_comments_cant_make_head_comment(self):
        challenge = Challenge.objects.get(id=1)
        juror = challenge.get_jurors()[0] # factory makes head comment for juror
        self.assertEqual(juror.can_make_head_comment(), False)
