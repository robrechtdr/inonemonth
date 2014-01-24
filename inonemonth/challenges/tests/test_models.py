import django.test
import unittest

from django.contrib.auth import get_user_model
from challenges.models import Challenge, Role


class ChallengesTestCase(django.test.TestCase):
    """
    Used to build data structure
    """
    def setUp(self):
        # Set up users
        albert = get_user_model().objects.create(email="albert@gmail.com",
                                                 username="albert",
                                                 password="my_password")
        sonya = get_user_model().objects.create(email="sonya@gmail.com",
                                                username="sonya",
                                                password="my_password")
        danny = get_user_model().objects.create(email="danny@gmail.com",
                                                username="danny",
                                                password="my_password")
        jimmy = get_user_model().objects.create(email="jimmy@gmail.com",
                                                username="jimmy",
                                                password="my_password")


        # Set up ssl_challenge, clencher and jurors
        ssl_challenge = Challenge.objects.create(title="I will do ssl shit",
                                                 body="my body",
                                                 repo_name="django_ssl")
        clencher_ssl_challenge = Role.objects.create(user=albert,
                                                     challenge=ssl_challenge,
                                                     type=Role.CLENCHER)
        juror1_ssl_challenge = Role.objects.create(challenge=ssl_challenge,
                                                   user=sonya,
                                                   type=Role.JUROR)
        juror2_ssl_challenge = Role.objects.create(challenge=ssl_challenge,
                                                   user=danny,
                                                   type=Role.JUROR)


        # Set up gargantuan_challenge, clencher and jurors
        gargantuan_challenge = Challenge.objects.create(title="I will do gargantuan shit",
                                                        body="my body",
                                                        repo_name="django_gargantuan")
        clencher_gargantuan_challenge = Role.objects.create(user=albert,
                                                            challenge=gargantuan_challenge,
                                                            type=Role.CLENCHER)
        juror1_gargantuan_challenge = Role.objects.create(challenge=gargantuan_challenge,
                                                          user=jimmy,
                                                          type=Role.JUROR)
        juror2_gargantuan_challenge = Role.objects.create(challenge=gargantuan_challenge,
                                                          user=sonya,
                                                          type=Role.JUROR)


    def test_get_clencher_from_challenge(self):
        ssl_challenge = Challenge.objects.get(repo_name="django_ssl")
        self.assertEqual(ssl_challenge.role_set.get(type="clencher"),
                         Role.objects.get(challenge=ssl_challenge,
                                          type=Role.CLENCHER)
        )


    def test_get_jurors_from_challenge(self):
        ssl_challenge = Challenge.objects.get(repo_name="django_ssl")
        # Why is complete queryset not equal even though it looks identical?
        self.assertEqual(ssl_challenge.get_jurors()[0],
                         # Filter because you get more than one result
                         Role.objects.filter(challenge=ssl_challenge,
                                             type=Role.JUROR)[0]
        )
