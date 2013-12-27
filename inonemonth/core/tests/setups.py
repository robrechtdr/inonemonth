import datetime
import factory
import factory.fuzzy
import random

from hashlib import sha1

from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

from userena.models import UserenaSignup
from userena.managers import UserenaManager

from profiles.models import Profile
from challenges.models import Challenge


class UserFactory(factory.DjangoModelFactory):
    """
    UserFactory class

    Don't use build method, would require changes to userena to implement.

    Only use tested methods that pass.
    """
    FACTORY_FOR = UserenaSignup
    # l112 https://github.com/bread-and-pepper/django-userena/blob/master/userena/forms.py
    username = factory.Sequence(lambda n: sha1(str(n)).hexdigest()[:5])
    email = factory.Sequence(lambda n: "john.doe{0}@gmail.com".format(n))
    password = "my_password"

    @classmethod
    def _create(cls, target_class, *args, **kwargs):
        """Overwrite _create to use UserenaSignup.objects.create_user"""
        manager = cls._get_manager(target_class)
        return manager.create_user(*args, **kwargs)


class JimUserFactory(UserFactory):
    email = "jim.klutz@gmail.com"


class JamesUserFactory(UserFactory):
    email = "james.narcis@gmail.com"


class ProfilePseudoFactory(factory.DjangoModelFactory):
    """
    Creates an inactive Profile.

    Profiles can't be created directly via Profiles,
    they need to be called via users.

    Defining a user class attribute creates two profiles at the same
    time per instantiation of ProfilePseudoFactory.

    Don't use build method, would require changes to userena to implement.

    Only use tested methods.
    """
    FACTORY_FOR = Profile

    @classmethod
    def _create(cls, target_class, *args, **kwargs):
        """Overwrite _create to use UserenaSignup.objects.create_user"""
        return UserFactory().profile


class ChallengeFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Challenge
    title = factory.Sequence(lambda n: "This is the title of challenge{0}.".format(n))
    description = factory.Sequence(lambda n: "This is the description of challenge{0}.".format(n))
    lincoln = factory.SubFactory(ProfilePseudoFactory)

    @factory.post_generation
    def judges(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for judge in extracted:
                self.judges.add(judge)
    #judges = factory.SubFactory(ProfileFactory)
