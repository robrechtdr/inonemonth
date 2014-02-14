from django.core.exceptions import ValidationError
from .github_utils import get_github_branch_url


class RepoExistanceValidator(object):
    def __init__(self, user):
        self.user = user

    def __call__(self, value):
        #self.user
        #value
        pass
