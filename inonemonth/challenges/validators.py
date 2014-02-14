from django.core.exceptions import ValidationError
from .github_utils import get_github_branch_url

# Problem, the validator should be able to access
# the user of the current page to get his account name/url!!
# But Can I do that with a validator?
def validate_repo_existance(value):
    """
    Raise a ValidationError if the repo doesn't exist.
    """
    pass
