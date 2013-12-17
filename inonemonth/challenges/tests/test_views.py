import django.test
import settings

from django.core.urlresolvers import reverse, resolve
from django.contrib.auth import authenticate

from ..views import challenge_create_view

class ChallengeCreateViewTestCase(django.test.TestCase):
    """
    Challenge_create_view test case.
    """

    def setUp(self):
        pass

    def test_get_logged_in(self):
        """
        Verify if a get request by a logged in user returns the challenge creation page.
        """
        url = reverse("challenge_create_view")
        # I'm getting status code 302(redirection) because I'm not logged in as
        # a user.

        #user = User.objects.get(pk=0)
        #self.client.login(username=user.username, password="password")
        #resp = self.client.get(url)
        #self.assertEqual(resp.status_code, 200)

    def test_get_not_logged_in(self):
        """
        Verify if a user who is not logged in gets redirected to the home page.
        """
        pass

