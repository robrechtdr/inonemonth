from __future__ import absolute_import

from optparse import make_option
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.providers import registry


def setup_site(domain):
    """
    >>> site = setup_site(domain="http://localhost")
    >>> site.name
    "localhost"
    """
    try:
        domain = domain
        name = domain.split("/")[-1] # derive from domain name
    except Exception:
        raise Exception("Display name failed to be derived from domain name")
    site, is_created= Site.objects.get_or_create(domain=domain, name=name)
    return site


def setup_github_social_app(social_app_name, site):
    """
    >>> site = setup_site(domain="http://localhost")
    >>> setup_github_social_app(social_app_name="github_app_local", site)
    """
    github_app, is_created = SocialApp.objects.get_or_create(
        provider="github", # See allauth.socialaccount.providers.
                           # registry.provider_map.keys()
        name = social_app_name,
        client_id = settings.ALLAUTH_SOCIAL_APP_GITHUB_ID,
        secret = settings.ALLAUTH_SOCIAL_APP_GITHUB_SECRET
    )
    github_app.sites.add(site)
    return github_app


def setup_site_and_github_social_app(domain, social_app_name):
    """
    >>> setup_site_and_github_social_app(
    ...     domain="http://localhost",
    ...     social_app_name="github_app_local"
    ... )

    Successive calls of this command do not create
    additional entries in Site and SocialApp.

    If github login doesn't work, check if you created a social access application
    on a Github account and if its ID and SECRET are identical to the one
    in settings.
    """
    site = setup_site(domain=domain)
    github_social_app = setup_github_social_app(social_app_name, site)


# Class MUST be named 'Command'
class Command(BaseCommand):
    help = "Create Site and SocialApp and tie them together"
    option_list = BaseCommand.option_list + (
        make_option("--domain",
            dest="domain",
            default="http://localhost",
        ),
        make_option("--social_app_name",
            dest="social_app_name",
            default="local_app",
        ),
    )

    def handle(self, *args, **options):
        social_providers = ["github"]
        if len(args) != 1:
            raise CommandError("you must specify an allauth supported "
                               "social provider (e.g. 'github')")
        if args[0] == social_providers[0]:
            setup_site_and_github_social_app(
                domain=options["domain"],
                social_app_name=options["social_app_name"]
            )
            self.stdout.write("Set up Github social app '{0}' to "
                              "domain '{1}'!".format(options["social_app_name"],
                                                     options["domain"]
                                             )
            )
        elif args[0] != social_providers[0]:
            raise CommandError("only the following social providers are currently supported: "
                               "{0}".format(", ".join(social_providers)))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
