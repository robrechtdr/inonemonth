import datetime
import factory
import factory.fuzzy
import random

from hashlib import sha1

from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

from challenges.models import Challenge, Role, Vote
from comments.models import HeadComment, TailComment

from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount


User = get_user_model()

class UserFactory(factory.DjangoModelFactory):
    FACTORY_FOR = User
    email = factory.Sequence(lambda n: 'john.doe{0}@gmail.com'.format(n))
    username = factory.LazyAttribute(lambda obj: obj.email.split("@")[0])
    password = "my_password"

    @factory.post_generation
    def set_email_address_object(self, create, extracted, **kwargs):
        EmailAddress.objects.create(user=self,
                                    email= self.email)


class RobrechtUserFactory(UserFactory):
    email = "robrecht.de.rouck@gmail.com"


class SocialUserFactory(factory.DjangoModelFactory):
    FACTORY_FOR = SocialAccount
    user = factory.SubFactory(UserFactory)
    provider = u"github"
    uid= u"1382556"
    extra_data = {u'avatar_url': u'https://gravatar.com/avatar/a13f182fbfe06570501700a310b5cf45?d=https%3A%2F%2Fidenticons.github.com%2F14e49a04ed384e716fcd708995faa62b.png&r=x',
                  u'bio': None,
                  u'blog': None,
                  u'company': None,
                  u'created_at': u'2012-08-15T10:56:03Z',
                  u'email': u'robrecht.de.rouck at gmail dot com',
                  u'events_url': u'https://api.github.com/users/RobrechtDR/events{/privacy}',
                  u'followers': 0,
                  u'followers_url': u'https://api.github.com/users/RobrechtDR/followers',
                  u'following': 0,
                  u'following_url': u'https://api.github.com/users/RobrechtDR/following{/other_user}',
                  u'gists_url': u'https://api.github.com/users/RobrechtDR/gists{/gist_id}',
                  u'gravatar_id': u'a13f182fbfe06570501700a310b5cf45',
                  u'hireable': False,
                  u'html_url': u'https://github.com/RobrechtDR',
                  u'id': 2156349,
                  u'location': u'Belgium',
                  u'login': u'RobrechtDR',
                  u'name': u'Robrecht De Rouck',
                  u'organizations_url': u'https://api.github.com/users/RobrechtDR/orgs',
                  u'public_gists': 1,
                  u'public_repos': 10,
                  u'received_events_url': u'https://api.github.com/users/RobrechtDR/received_events',
                  u'repos_url': u'https://api.github.com/users/RobrechtDR/repos',
                  u'site_admin': False,
                  u'starred_url': u'https://api.github.com/users/RobrechtDR/starred{/owner}{/repo}',
                  u'subscriptions_url': u'https://api.github.com/users/RobrechtDR/subscriptions',
                  u'type': u'User',
                  u'updated_at': u'2014-01-29T22:27:37Z',
                  u'url': u'https://api.github.com/users/RobrechtDR'}


    @classmethod
    def _create(cls, target_class, *args, **kwargs):
        """Override the default ``_create`` with our custom call."""
        manager = cls._get_manager(target_class)
        # The default would use ``manager.create(*args, **kwargs)``
        social_account = manager.create(*args, **kwargs)
        return social_account.user


class RobrechtSocialUserFactory(SocialUserFactory):
    user = factory.SubFactory(RobrechtUserFactory)
    uid= u"2156349"


class ChallengeFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Challenge
    title = factory.Sequence(lambda n: "This is the title of the challenge{0}.".format(n))
    body = factory.Sequence(lambda n: "This is the body of the challenge{0}.".format(n))
    repo_name = factory.Sequence(lambda n: "project{0}.".format(n))


class ClencherRoleFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Role
    user = factory.SubFactory(SocialUserFactory)
    type = "clencher"
    challenge = factory.SubFactory(ChallengeFactory)


class RobrechtClencherRoleFactory(ClencherRoleFactory):
    user = factory.SubFactory(RobrechtSocialUserFactory)
    challenge = factory.SubFactory(ChallengeFactory)


class JurorRoleFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Role
    user = factory.SubFactory(UserFactory)
    type = "juror"
    challenge = factory.SubFactory(ChallengeFactory)


class VoteFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Vote
    decision = "positive"
    juror = factory.SubFactory(JurorRoleFactory)


class HeadCommentFactory(factory.DjangoModelFactory):
    FACTORY_FOR = HeadComment
    text = factory.Sequence(lambda n: "This is head comment {0}.".format(n))
    owner = factory.SubFactory(JurorRoleFactory)
    challenge = factory.SubFactory(ChallengeFactory)


class TailCommentFactory(factory.DjangoModelFactory):
    FACTORY_FOR = TailComment
    text = factory.Sequence(lambda n: "This is tail comment {0}.".format(n))
    owner = factory.SubFactory(ClencherRoleFactory)
    challenge = factory.SubFactory(ChallengeFactory)
    head = factory.SubFactory(HeadCommentFactory)


class GargantuanChallengeFactory(ChallengeFactory):
    title = "Gargantuan project challenge"
    body = "Gargantuan is the first project where I implement an api"
    repo_name = "gargantuan"

    @factory.post_generation
    def set_email_address_object(self, create, extracted, **kwargs):
        clencher = RobrechtClencherRoleFactory(challenge=self)

        juror1 = JurorRoleFactory(challenge=self)
        head1 = HeadCommentFactory(text="I think you succeeded!",
                                   owner=juror1,
                                   challenge=self)
        VoteFactory(decision="positive", juror=juror1)

        juror2 = JurorRoleFactory(challenge=self)
        head2 = HeadCommentFactory(text="I think you failed!",
                                   owner=juror2,
                                   challenge=self)
        VoteFactory(decision="negative", juror=juror2)

        TailCommentFactory(text="I don't agree.",
                           owner=juror1,
                           challenge=self,
                           head=head1)

        TailCommentFactory(text="I don't agree either!",
                           owner=juror2,
                           challenge=self,
                           head=head1)
