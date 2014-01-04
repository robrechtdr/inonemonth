from django.contrib.auth.decorators import user_passes_test
from django.core.urlresolvers import reverse, reverse_lazy

def has_profile(user):
    """
    Check if user has profile.

    Anonymous users don't have profiles.
    """
    return hasattr(user, "profile")

user_has_profile = user_passes_test(has_profile, reverse_lazy("home_view"))
