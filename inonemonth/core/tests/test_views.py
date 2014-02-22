from __future__ import absolute_import

import django.test
import settings

from django.core.urlresolvers import reverse, resolve
from django.contrib.auth import authenticate


class HomeViewTestCase(django.test.TestCase):
    url = "/"

    '''
    def test_url_resolves_to_view(self):
        found = resolve(self.url)
        #self.assertEqual(found.func, home_view)
        self.assertEqual(found.func, userena.views.signin)
    '''

    def test_url_success_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_url_response_contains_html_tag(self):
        response = self.client.get(self.url)
        self.assertIn("<html", response.content)


class SignupViewTestCase(django.test.TestCase):
    def setUp(self):
        # https://github.com/pennersr/django-allauth/blob/master/allauth/account/tests.py#L37-L56
        '''
        from allauth.socialaccount.models import SocialApp
        social_account = SocialApp.objects.create(name="github_app",
                                                  provider="github")
        social_account.add(Site.objects.get_current())

        user = User.objects.create(email='jason@raymond.penners')
        user.name = user.email.split("@")[0]
        user.set_password('password')
        user.save()
        EmailAddress.objects.create(email=user.email,
                                    primary=True,
                                    verified=True)

        '''
        pass
