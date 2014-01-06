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
