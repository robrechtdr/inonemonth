from __future__ import absolute_import

import unittest
import django.test

from django.core.urlresolvers import reverse
from django.core import mail

from .setups import GargantuanChallengeFactory
from ..mail_utils import (send_invitation_mail_to_juror,
                          build_url_base, build_absolute_url)


class EmailUtilsTestCase(django.test.TestCase):
    def setUp(self):
        request_factory = django.test.RequestFactory()
        self.path = reverse("challenge_invite_jurors_view", kwargs={"pk":1})
        self.request = request_factory.get(self.path)

    def test_build_url_base(self):
        self.assertEqual(build_url_base(self.request), "http://testserver")

    def test_build_absolute_url(self):
        url_base = build_url_base(self.request)
        self.assertEqual(build_absolute_url(url_base, self.path), "http://testserver/challenge/1/invite-jurors/")


class SendInvitationMailToJurorTestCase(django.test.TestCase):
    def setUp(self):
        request_factory = django.test.RequestFactory()
        request = request_factory.get(reverse("challenge_invite_jurors_view", kwargs={"pk":1}))
        self.url_base = build_url_base(request)
        challenge = GargantuanChallengeFactory()
        self.juror = challenge.get_jurors()[0]

    def test_send_invitation_mail_to_juror_new(self):
        text = ('de.rouck.robrecht@gmail.com has invited you to be a juror '
                'for the following challenge:\n\n'
                'Gargantuan project challenge\n\n'
                'Go to this challenge via '
                'http://testserver/account/signin-juror/challenge/1/\n\n'
                'Login credentials:\n'
                'Email: andy.slacker@gmail.com\n'
                'Password: temp_password\n\n'
                'Note that it is advised to change your password.\n')

        send_invitation_mail_to_juror(juror=self.juror, url_base=self.url_base,
                                      juror_registered=False)
        self.assertEqual(len(mail.outbox), 1)
        email = mail.outbox[0]
        self.assertEqual(email.to,["andy.slacker@gmail.com"])
        self.assertEqual(email.from_email,"de.rouck.robrecht@gmail.com")
        self.assertEqual(email.body, text)

    def test_send_invitation_mail_to_juror_registered(self):
        text = ('de.rouck.robrecht@gmail.com has invited you to be a juror '
                'for the following challenge:\n\n'
                'Gargantuan project challenge\n\n'
                'Go to this challenge via '
                'http://testserver/account/signin-juror/challenge/1/\n\n')

        send_invitation_mail_to_juror(juror=self.juror, url_base=self.url_base,
                                      juror_registered=True)
        self.assertEqual(len(mail.outbox), 1)
        email = mail.outbox[0]
        self.assertEqual(email.to,["andy.slacker@gmail.com"])
        self.assertEqual(email.from_email,"de.rouck.robrecht@gmail.com")
        self.assertEqual(email.body, text)
