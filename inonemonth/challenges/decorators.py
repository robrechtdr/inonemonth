from django.contrib.auth.decorators import user_passes_test
from django.core.urlresolvers import reverse, reverse_lazy


def has_github_account(user):
    try:
        if user.socialaccount_set.all():
            return True
        else:
            return False
    # In case of an anonymous user, which has
    # no socialaccount_set attribute
    except AttributeError:
        return False

user_has_github_account = user_passes_test(has_github_account,
                                           login_url=reverse_lazy("socialaccount_connections"))
