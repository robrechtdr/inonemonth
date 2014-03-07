from __future__ import absolute_import

import django.test

from ..github_utils import (get_api_repo_branch_url,
                            get_repo_and_branch_from_repo_path,
                            get_main_branch_url,
                            get_last_commit_on_branch,
                            get_commit_comparison_url)


class GithubUtilsTestCase(django.test.TestCase):
    def test_get_api_repo_branch_url(self):
        github_login = "RobrechtDR"
        repo = "asiakas"
        branch = "master"
        repo_url = get_api_repo_branch_url(github_login, repo, branch)
        self.assertEqual(
            repo_url,
            "https://api.github.com/repos/RobrechtDR/asiakas/branches/master")

    def test_get_repo_and_branch_from_repo_path_1(self):
        repo_and_branch_from_path = get_repo_and_branch_from_repo_path(
            "asiakas/master")
        self.assertEqual(repo_and_branch_from_path, ("asiakas", "master"))

    def test_get_repo_and_branch_from_repo_path_2(self):
        repo_and_branch_from_path = get_repo_and_branch_from_repo_path(
            "asiakas")
        self.assertEqual(repo_and_branch_from_path, ("asiakas", "master"))

    def test_get_repo_and_branch_from_repo_path_3(self):
        repo_and_branch_from_path = get_repo_and_branch_from_repo_path(
            "asiakas/feature/registration")
        self.assertEqual(repo_and_branch_from_path,
                         ("asiakas", "feature/registration"))

    def test_get_main_branch_url(self):
        target_url = "https://github.com/RobrechtDR/asiakas/tree/master"
        self.assertEqual(
            get_main_branch_url("RobrechtDR", "asiakas", "master"),
            target_url)

    def test_get_last_commit_on_branch(self):
        # Project is moved so there are likely no new commits
        # TODO: Replace with my own test github project later
        github_login = "dnerdy"
        repo_name = "factory_boy"
        branch_name = "master"
        self.assertEqual(
            get_last_commit_on_branch(github_login, repo_name, branch_name),
            '638704c06e7f3bc6412f2c81fe5b3073b397a60b')

    def test_get_commit_comparison_url(self):
        owner = "RobrechtDR"
        repo = "asiakas"
        start_commit = "6b8c19067"
        end_commit = "b3e18963c3"
        self.assertEqual(
            get_commit_comparison_url(owner, repo, start_commit, end_commit),
            ("https://github.com/RobrechtDR/asiakas/"
             "compare/6b8c19067...b3e18963c3"))
