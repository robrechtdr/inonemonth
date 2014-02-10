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


class ChallengeTestCase(django.test.TestCase):
    def setUp(self):
        call_command('setup_allauth_social', 'github', domain="http://localhost", setting="test")
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
        self.assertEqual(challenge.get_clencher().user.email, u"de.rouck.robrecht@gmail.com")

    def test_get_jurors(self):
        GargantuanChallengeFactory()
        challenge = Challenge.objects.get(id=1)
        self.assertEqual([juror.user.email for juror in challenge.get_jurors()],
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

    @unittest.skip("")
    def test_get_juror_representation_list(self):
        GargantuanChallengeFactory()
        challenge = Challenge.objects.get(id=1)

        '''
        from mock import Mock
        juror_mock = Mock(spec=Role)
        #juror_mock.return_value = "<Role: Juror "#'{0}' of '{1}'"#.format(..)
        #juror_mock.return_value = "<Role: {0}".format(Role.__unicode__(juror# "#'{0}' of '{1}'"#.format(..)
        #andy_mock = juror_mock(username="andy.slacker", challenge="Challenge 1")
        juror_mock.type = "kok"
        juror_mock.user = "my_user"
        juror_mock.challenge = "my_chal"
        my_jur = Role.__unicode__(juror_mock)
        import pdb; pdb.set_trace()
        '''
        self.assertEqual(challenge.get_juror_representation_list(), "")


class RoleTestCase(django.test.TestCase):
    def setUp(self):
        call_command('setup_allauth_social', 'github', domain="http://localhost", setting="test")
        #GargantuanChallengeFactory()

    def tearDown(self):
        UserFactory.reset_sequence(1)

    def test_get_unicode(self):
        TimeFixedGargantuanChallengeFactory()
        challenge = Challenge.objects.get(id=1)
        clencher = challenge.get_clencher()
        self.assertEqual(clencher.__unicode__(),
                         "Clencher 'de.rouck.robrecht' of 'Challenge 1, created on Tue Feb  4 09:15:00 2014'")

    def test_get_absolute_url(self):
        GargantuanChallengeFactory()
        challenge = Challenge.objects.get(id=1)
        clencher = challenge.get_clencher()
        self.assertEqual(clencher.get_absolute_url(), "/api/roles/1/")

    def test_clencher_cant_make_head_comment(self):
        GargantuanChallengeFactory()
        challenge = Challenge.objects.get(id=1)
        clencher = challenge.get_clencher()
        self.assertEqual(clencher.can_make_head_comment(), False)

    def test_is_juror(self):
        GargantuanChallengeFactory()
        challenge = Challenge.objects.get(id=1)
        juror = challenge.get_jurors()[0]
        self.assertEqual(juror.is_juror(), True)

    def test_clencher_cant_make_head_comment(self):
        GargantuanChallengeFactory()
        challenge = Challenge.objects.get(id=1)
        clencher = challenge.get_clencher()
        self.assertEqual(clencher.can_make_head_comment(), False)

    def test_juror_cant_make_head_comment_before_end_of_challenge_period(self):
        GargantuanChallengeFactory()
        challenge = Challenge.objects.get(id=1)
        jason = User.objects.get(email="jason.jay@gmail.com")
        juror_jason = challenge.role_set.get(user=jason) # without head comment
        self.assertEqual(juror_jason.can_make_head_comment(), False)
        # While:
        self.assertEqual(challenge.in_challenge_period(), True)

    def test_juror_without_headcomments_can_make_head_comment(self):
        InVotingPeriodGargantuanChallengeFactory()
        challenge = Challenge.objects.get(id=1)
        jason = User.objects.get(email="jason.jay@gmail.com")
        juror_jason = challenge.role_set.get(user=jason) # without head comment
        self.assertEqual(juror_jason.can_make_head_comment(), True)

    def test_juror_with_comments_cant_make_head_comment(self):
        GargantuanChallengeFactory()
        challenge = Challenge.objects.get(id=1)
        andy = User.objects.get(email="andy.slacker@gmail.com")
        juror_andy = challenge.role_set.get(user=andy) # with head comment
        self.assertEqual(juror_andy.can_make_head_comment(), False)

    def test_juror_get_challenge_representation_for_juror(self):
        GargantuanChallengeFactory()
        challenge = Challenge.objects.get(id=1)
        andy = User.objects.get(email="andy.slacker@gmail.com")
        juror_andy = challenge.role_set.get(user=andy)
        juror_representation_for_juror = juror_andy.get_challenge_representation_for_juror()
        self.assertEqual(juror_representation_for_juror, "Juror 1")

    def test_clencher_get_challenge_representation_for_juror(self):
        GargantuanChallengeFactory()
        challenge = Challenge.objects.get(id=1)
        clencher = challenge.get_clencher()
        clencher_representation_for_juror = clencher.get_challenge_representation_for_juror()
        self.assertEqual(clencher_representation_for_juror, "Clencher")
