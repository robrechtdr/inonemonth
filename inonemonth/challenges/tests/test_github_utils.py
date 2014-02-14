import unittest
import django.test
from ..github_utils import (get_api_repo_branch_url,
                            get_repo_and_branch_from_repo_path)

class GithubUtilsTestCase(django.test.TestCase):
    def test_get_api_repo_branch_url(self):
        github_login = "RobrechtDR"
        repo = "asiakas"
        branch = "master"
        repo_url = get_api_repo_branch_url(github_login, repo, branch)
        self.assertEqual(repo_url, "https://api.github.com/repos/RobrechtDR/asiakas/branches/master")

    def test_get_repo_and_branch_from_repo_path_1(self):
        repo_and_branch_from_path = get_repo_and_branch_from_repo_path("asiakas/master")
        self.assertEqual(repo_and_branch_from_path, ("asiakas", "master"))

    def test_get_repo_and_branch_from_repo_path_2(self):
        repo_and_branch_from_path = get_repo_and_branch_from_repo_path("asiakas")
        self.assertEqual(repo_and_branch_from_path, ("asiakas", "master"))

    def test_get_repo_and_branch_from_repo_path_3(self):
        repo_and_branch_from_path = get_repo_and_branch_from_repo_path("asiakas/feature/registration")
        self.assertEqual(repo_and_branch_from_path, ("asiakas", "feature/registration"))
