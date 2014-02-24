import unittest
import django.test

from django.contrib.auth.models import AnonymousUser

from core.tests.setups import (RobrechtClencherRoleFactory,
                               JurorRoleFactory)
from ..decorators import authenticated_user_has_github_account


class HasGithubAccountTestCase(django.test.TestCase):
    def test_authenticated_user_has_github_account1(self):
        clencher = RobrechtClencherRoleFactory()
        user = clencher.user
        self.assertTrue(authenticated_user_has_github_account(user))

    def test_authenticated_user_has_github_account2(self):
        # A juror (has no social account but has socialaccount_set attr)
        user = JurorRoleFactory().user
        self.assertFalse(authenticated_user_has_github_account(user))

    def test_authenticated_user_has_github_account3(self):
        # An anonymous user (has no socialaccount_set attribute)
        user = AnonymousUser()
        self.assertTrue(authenticated_user_has_github_account(user))
