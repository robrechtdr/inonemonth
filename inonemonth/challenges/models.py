from django.db import models
from django.contrib.auth import get_user_model


class Challenge(models.Model):
    """
    """
    # Use placeholder: one line description of what you want to achieve
    title = models.CharField(max_length=200)
    body = models.TextField()
    repo_name = models.CharField(max_length=200)
    creation_datetime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "Challenge created on {0} by {1}".format(
            self.creation_datetime.ctime(),
            self.clencher.user
        )
        #return "In one month {0}".format(self.title)

    def get_user_role(self, user):
        if user == self.clencher.user:
            return self.clencher
        elif user in self.juror_set.all():
            return self.juror_set.get(user=user)
        else:
            raise Exception("User '{0}' does not have a role for "
                            "this challenge".format(user.__unicode__()))


class ChallengeRole(models.Model):
    """
    Abstract class ChallengeRole

    A role instance for a given challenge is attached to one user at maximum and a user
    can have many instances of a role of different challenges.
    """
    user = models.ForeignKey(get_user_model()) # Is get_user_model correct here or other name with allauth?

    class Meta:
        abstract = True


class Clencher(ChallengeRole):
    """
    """
    challenge = models.OneToOneField(Challenge)

    def __unicode__(self):
        return "Clencher {0} of {1}".format(self.user, self.challenge)


class Juror(ChallengeRole):
    """
    """
    challenge = models.ForeignKey(Challenge)
    positive_vote = models.NullBooleanField(null=True, blank=True)

    def __unicode__(self):
        return "Juror {0} in {1}".format(self.user, self.challenge)
