from __future__ import absolute_import

import django.test

from urlparse import urlparse
from django.conf import settings
from django.core.urlresolvers import reverse, reverse_lazy, resolve
from django.contrib.auth import authenticate

#!! from core.tests.setups import UserFactory, ChallengeFactory

from ..views import challenge_create_view, challenge_detail_view
from ..models import Challenge


class ChallengeCreateViewTestCase(django.test.TestCase):
    """
    Challenge_create_view test case.
    """
    def setUp(self):
        pass

    '''
    def test_get_request_non_logged_in_user_redirects(self):
        """
        Verify if a get request of a non logged in user redirects to page
        with login.
        """
        url = reverse("challenge_create_view")
        response = self.client.get(url, follow=True)
        # Test if there is a redirect
        self.assertTrue(response.redirect_chain,
                        msg="view should redirect")

        # Test if redirects to home page (which has login)
        full_url_redirect = response.redirect_chain[0][0]
        relative_url_redirect = urlparse(full_url_redirect).path
        self.assertEqual(relative_url_redirect, reverse("home_view"))
    '''

    def test_get_request_logged_in_user_does_not_redirect(self):
        '''
        url = reverse("challenge_create_view")
        inactive_user = UserFactory()
        # Activate user (same as confirming account with link in activation
        # email)
        #!! active_user = UserenaSignup.objects.activate_user(inactive_user.userena_signup.activation_key)
        #!! self.client.login(username=active_user.username, password="my_password", email=active_user.email)
        response = self.client.get(url)
        #!! self.assertEqual(response.status_code, 200)
        '''

class ChallengeDetailViewTestCase(django.test.TestCase):
    """
    Challenge_detail_view test case.
    """
    def test_url_resolves_to_view(self):
        """
        found = resolve("/challenges/1/detail/")
        #self.assertEqual(found.func, challenge_detail_view)
        self.assertEqual(found.func.func_name, ChallengeDetailView.as_view().func_name)
        """

    def test_detail_view(self):
        pass
        '''
        # Create challenge. Can't view a challenge that doesn't exist yet ##
        inactive_user = UserFactory()
        #!! active_user = UserenaSignup.objects.activate_user(inactive_user.userena_signup.activation_key)
        #!! Challenge.objects.create(title="My challenge",
        #                         body="This is my challenge",
        #                         clencher=active_user.profile)
        ####################################################################
        url = reverse("challenge_detail_view", kwargs={"pk": 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        '''
