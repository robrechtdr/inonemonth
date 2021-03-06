from __future__ import absolute_import

import django.test
import unittest

from django.core.management import call_command
from django.contrib.auth import get_user_model
from challenges.models import Challenge

from core.tests.setups import (GargantuanChallengeFactory,
                               ChallengeFactory, UserFactory,
                               TimeFixedGargantuanChallengeFactory,
                               InVotingPeriodGargantuanChallengeFactory,
                               EndedGargantuanChallengeFactory,
                               RobrechtClencherRoleFactory)


User = get_user_model()


class ChallengeTestCase(django.test.TestCase):
    def setUp(self):
        call_command('setup_allauth_social',
                     'github',
                     domain="http://localhost",
                     setting="test")
        #GargantuanChallengeFactory()

    def tearDown(self):
        UserFactory.reset_sequence(1)

    def test_get_unicode(self):
        TimeFixedGargantuanChallengeFactory()
        challenge = Challenge.objects.get(id=1)
        self.assertEqual(challenge.__unicode__(),
                         "Challenge 1, created on Tue Feb  4 09:15:00 2014")

    def test_get_absolute_url(self):
        GargantuanChallengeFactory()
        challenge = Challenge.objects.get(id=1)
        self.assertEqual(challenge.get_absolute_url(), "/api/challenges/1/")

    def test_get_clencher(self):
        GargantuanChallengeFactory()
        challenge = Challenge.objects.get(id=1)
        self.assertEqual(challenge.get_clencher().user.email,
                         u"de.rouck.robrecht@gmail.com")

    def test_get_jurors(self):
        GargantuanChallengeFactory()
        challenge = Challenge.objects.get(id=1)
        self.assertEqual(
            [juror.user.email for juror in challenge.get_jurors()],
            [u'andy.slacker@gmail.com', u'fred.labot@gmail.com',
             u'jason.jay@gmail.com'])

    def test_get_challenge_period_end_datetime(self):
        TimeFixedGargantuanChallengeFactory()
        challenge = Challenge.objects.get(id=1)
        self.assertEqual(challenge.get_challenge_period_end_datetime().ctime(),
                         'Tue Mar  4 09:15:00 2014')
        # While:
        self.assertEqual(challenge.creation_datetime.ctime(),
                         'Tue Feb  4 09:15:00 2014')

    def test_get_voting_period_end_datetime(self):
        TimeFixedGargantuanChallengeFactory()
        challenge = Challenge.objects.get(id=1)
        # Weird: why is there no space here in ctime format? Or rather why
        # was there a space in
        # challenge.get_challenge_period_end_datetime().ctime() ?
        self.assertEqual(challenge.get_voting_period_end_datetime().ctime(),
                         'Tue Mar 11 09:15:00 2014')
        # While:
        self.assertEqual(challenge.creation_datetime.ctime(),
                         'Tue Feb  4 09:15:00 2014')

    def test_in_voting_period(self):
        InVotingPeriodGargantuanChallengeFactory()
        challenge = Challenge.objects.get(id=1)
        self.assertEqual(challenge.in_voting_period(), True)

    def test_in_challenge_period(self):
        GargantuanChallengeFactory()
        challenge = Challenge.objects.get(id=1)
        self.assertEqual(challenge.in_challenge_period(), True)

    def test_has_challenge_ended(self):
        EndedGargantuanChallengeFactory()
        challenge = Challenge.objects.get(id=1)
        self.assertEqual(challenge.has_ended(), True)

    def test_get_juror_representation_number_as_juror(self):
        EndedGargantuanChallengeFactory()
        challenge = Challenge.objects.get(id=1)
        juror_1 = challenge.get_jurors()[0]
        self.assertEqual(challenge.get_juror_representation_number(juror_1), 1)

    def test_get_juror_representation_number_as_non_juror_for_given_challenge(self):
        EndedGargantuanChallengeFactory()
        challenge = Challenge.objects.get(id=1)
        clencher = challenge.get_clencher()
        self.assertRaises(Exception,
                          challenge.get_juror_representation_number, clencher)

    def test_get_vote_results(self):
        EndedGargantuanChallengeFactory()
        challenge = Challenge.objects.get(id=1)
        self.assertEqual(challenge.get_vote_results(),
                         {'positive': 1, 'negative': 1, 'not_voted': 1})

    # Need more tests for tested method
    def test_has_majority_vote(self):
        EndedGargantuanChallengeFactory()
        challenge = Challenge.objects.get(id=1)
        self.assertEqual(challenge.has_majority_vote(), False)

    # Need more tests for tested method
    def test_is_successful(self):
        EndedGargantuanChallengeFactory()
        challenge = Challenge.objects.get(id=1)
        self.assertEqual(challenge.is_successful(), False)

    def test_get_repo_branch_path_representation(self):
        challenge = ChallengeFactory(repo_name="asiakas", branch_name="master")
        self.assertEqual(challenge.get_repo_branch_path_representation(),
                         "asiakas/master")

    def test_get_branch_main_url(self):
        clencher_rob = RobrechtClencherRoleFactory()
        challenge = clencher_rob.challenge
        self.assertEqual(
            challenge.get_branch_main_url(),
            "https://github.com/RobrechtDR/gargantuan/tree/challenge")

    @unittest.skip("The challenge method currently makes a request")
    def test_get_commit_comparison_url(self):
        challenge = GargantuanChallengeFactory(repo_name="asiakas",
                                               branch_name="master",
                                               start_commit="6b8c19067")
        self.assertEqual(
            challenge.get_commit_comparison_url(),
            ("https://github.com/RobrechtDR/asiakas/"
             "compare/6b8c19067...b3e18963c3e1091134f5b4637aa198d196336ea9"))

    def test_is_last_commit_different_from_start_commit(self):
        challenge = GargantuanChallengeFactory(repo_name="asiakas",
                                               branch_name="master",
                                               start_commit="6b8c19067")
        self.assertEqual(
            challenge.is_last_commit_different_from_start_commit(),
            True)

    def test_user_has_role(self):
        challenge = GargantuanChallengeFactory()
        rob = challenge.get_clencher().user
        self.assertEqual(challenge.user_has_role(rob), True)


class RoleTestCase(django.test.TestCase):
    def setUp(self):
        call_command('setup_allauth_social',
                     'github',
                     domain="http://localhost",
                     setting="test")
        #GargantuanChallengeFactory()

    def tearDown(self):
        UserFactory.reset_sequence(1)

    def test_get_unicode(self):
        TimeFixedGargantuanChallengeFactory()
        challenge = Challenge.objects.get(id=1)
        clencher = challenge.get_clencher()
        self.assertEqual(
            clencher.__unicode__(),
            ("Clencher 'de.rouck.robrecht' of 'Challenge 1, "
             "created on Tue Feb  4 09:15:00 2014'"))

    def test_get_absolute_url(self):
        GargantuanChallengeFactory()
        challenge = Challenge.objects.get(id=1)
        clencher = challenge.get_clencher()
        self.assertEqual(clencher.get_absolute_url(), "/api/roles/1/")

    def test_is_juror(self):
        GargantuanChallengeFactory()
        challenge = Challenge.objects.get(id=1)
        juror = challenge.get_jurors()[0]
        self.assertTrue(juror.is_juror())
        clencher = challenge.get_clencher()
        self.assertFalse(clencher.is_juror())

    def test_clencher_cant_make_head_comment(self):
        GargantuanChallengeFactory()
        challenge = Challenge.objects.get(id=1)
        clencher = challenge.get_clencher()
        self.assertEqual(clencher.can_make_head_comment(), False)

    def test_juror_cant_make_head_comment_before_end_of_challenge_period(self):
        GargantuanChallengeFactory()
        challenge = Challenge.objects.get(id=1)
        jason = User.objects.get(email="jason.jay@gmail.com")
        juror_jason = challenge.role_set.get(user=jason)  # without head comment
        self.assertEqual(juror_jason.can_make_head_comment(), False)
        # While:
        self.assertEqual(challenge.in_challenge_period(), True)

    def test_juror_without_headcomments_can_make_head_comment(self):
        InVotingPeriodGargantuanChallengeFactory()
        challenge = Challenge.objects.get(id=1)
        jason = User.objects.get(email="jason.jay@gmail.com")
        juror_jason = challenge.role_set.get(user=jason)  # without head comment
        self.assertEqual(juror_jason.can_make_head_comment(), True)

    def test_juror_with_comments_cant_make_head_comment(self):
        GargantuanChallengeFactory()
        challenge = Challenge.objects.get(id=1)
        andy = User.objects.get(email="andy.slacker@gmail.com")
        juror_andy = challenge.role_set.get(user=andy)  # with head comment
        self.assertEqual(juror_andy.can_make_head_comment(), False)
