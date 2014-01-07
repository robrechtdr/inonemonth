import datetime
import factory
import factory.fuzzy
import random

from hashlib import sha1

from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

from challenges.models import Challenge


class UserFactory(factory.DjangoModelFactory):
    """
    UserFactory class

    Don't use build method, would require changes to userena to implement.

    Only use tested methods that pass.
    """
    pass

    '''
    FACTORY_FOR = get_user_model()
    email = factory.Sequence(lambda n: "john.doe{0}@gmail.com".format(n))
    password = "my_password"
    '''


class JimUserFactory(UserFactory):
    email = "jim.klutz@gmail.com"


class JamesUserFactory(UserFactory):
    email = "james.narcis@gmail.com"


'''
class ChallengeFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Challenge
    title = factory.Sequence(lambda n: "This is the title description of challenge{0}.".format(n))
    body = factory.Sequence(lambda n: "This is the body description of challenge{0}.".format(n))
    clencher = factory.SubFactory(ProfilePseudoFactory)

    @factory.post_generation
    def jurors(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for judge in extracted:
                self.jurors.add(judge)
    #jurors = factory.SubFactory(ProfileFactory)
'''
