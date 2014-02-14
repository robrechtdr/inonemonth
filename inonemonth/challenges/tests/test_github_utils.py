import unittest
import django.test


class GithubUtilsTestCase(django.test.TestCase):
    def test_get_api_repo_branch_url(self):
        self.assertEqual("", "https://api.github.com/repos/RobrechtDR/asiakas/branches/master")

    def test_get_repo_and_branch_from_repo_path(self):
        self.assertEqual("", ("asiakas", "master"))
