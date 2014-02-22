from __future__ import absolute_import

import requests

from django.core.exceptions import ValidationError
from .github_utils import get_api_repo_branch_url, get_repo_and_branch_from_repo_path


class RepoExistanceValidator(object):
    def __init__(self, user):
        self.user = user

    def __call__(self, value):
        github_social_account = self.user.socialaccount_set.get(id=1)
        github_login = github_social_account.extra_data["login"]
        repo_name, branch = get_repo_and_branch_from_repo_path(value)
        repo_url = get_api_repo_branch_url(github_login, repo_name, branch)
        repo_req = requests.get(repo_url)
        if repo_req.status_code == 200:
            pass
        elif repo_req.status_code == 404:
            raise ValidationError("This repo does not exist on your Github account")
        else:
            raise Exception("Else die")
