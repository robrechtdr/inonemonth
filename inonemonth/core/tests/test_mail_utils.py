import unittest
import django.test

from django.core.urlresolvers import reverse
from django.core import mail

from .setups import GargantuanChallengeFactory
from ..mail_utils import send_invitation_mail_to_juror


class EmailUtilsTestCase(django.test.TestCase):
    def test_send_invitation_mail_to_juror(self):
        request_factory = django.test.RequestFactory()
        request = request_factory.get(reverse("challenge_invite_jurors_view", kwargs={"pk":1}))
        challenge = GargantuanChallengeFactory()
        juror = challenge.get_jurors()[0] # Gets juror andy.slacker@gmail.com
        send_invitation_mail_to_juror(juror, request)
        self.assertEqual(len(mail.outbox), 1)
        email = mail.outbox[0]
        self.assertEqual(email.to,["andy.slacker@gmail.com"])
        self.assertEqual(email.from_email,"de.rouck.robrecht@gmail.com")
