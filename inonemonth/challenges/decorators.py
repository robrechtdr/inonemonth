from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import user_passes_test


def authenticated_user_has_github_account(user):
    try:
        if user.socialaccount_set.all():
            return True
        else:
            return False
    # In case of an anonymous user(non-authenticated),
    # which has no socialaccount_set attribute
    except AttributeError:
        return True

auth_user_has_github_account = user_passes_test(
    authenticated_user_has_github_account,
    login_url=reverse_lazy("socialaccount_connections"))
