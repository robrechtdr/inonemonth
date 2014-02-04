from dateutil.relativedelta import relativedelta

from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse, reverse_lazy


class Challenge(models.Model):
    """
    """
    # Use placeholder: one line description of what you want to achieve
    title = models.CharField(max_length=200)
    body = models.TextField()
    repo_name = models.CharField(max_length=200)
    creation_datetime = models.DateTimeField(auto_now_add=True)

    # Don"t include self.role_set.user because the user will not exist
    # in some cases.
    def __unicode__(self):
        return "Challenge {0}, created on {1}".format(
            self.id,
            self.creation_datetime.ctime()
        )

    def get_absolute_url(self):
        return reverse("challenge_api_retrieve", kwargs={"pk": self.pk})

    def get_clencher(self):
        try:
            return self.role_set.get(type=self.role_set.model.CLENCHER)
        except ObjectDoesNotExist:
            raise Exception("No user has been assigned as clencher "
                                  "for this challenge yet.")

    # Make manager method out of it, but will I then be able to use it in
    # serializer?
    def get_jurors(self):
        # `filter` call with no results returns an empty list (vs `get`)
        jurors = self.role_set.filter(type=self.role_set.model.JUROR)
        if jurors:
            return jurors
        else:
            return self.Exception("No Juror has been assigned as juror "
                                     "for this challenge yet.")

    def get_challenge_period_end_datetime(self):
        #one_month = relativedelta(months=1)
        one_month = relativedelta(days=1)
        #one_month = relativedelta(minutes=20)
        return (self.creation_datetime + one_month)

    def get_voting_period_end_datetime(self):
        #one_month = relativedelta(months=1)
        one_week = relativedelta(weeks=1)
        #one_month = relativedelta(minutes=20)
        return (self.get_challenge_period_end_datetime() + one_week)


class Role(models.Model):
    """
    Role for a given challenge: Clencher or Juror.
    A role instance for a given challenge is attached to one user at maximum.
    """
    CLENCHER = "clencher" # is more descriptive than a single capital in js
    JUROR = "juror"
    ROLE_CHOICES = ((CLENCHER, CLENCHER.capitalize()),
                    (JUROR, JUROR.capitalize()))

    user = models.ForeignKey(get_user_model())
    type = models.CharField(max_length=10, choices=ROLE_CHOICES)
    challenge = models.ForeignKey(Challenge)

    def __unicode__(self):
        return "{0} '{1}' of '{2}'".format(self.type.capitalize(), self.user, self.challenge)

    def get_absolute_url(self):
        return reverse("role_api_retrieve", kwargs={"pk": self.pk})

    # Possibly refine later, to only allow jurors to vote during
    # the judgement period.
    def can_vote(self):
        if self.type == self.JUROR:
            return True
        elif self.type == self.CLENCHER:
            return False

    def can_make_head_comment(self):
        """
        Only allow jurors that haven't made a head comment yet to make a head
        comment.
        """
        if self.type == self.JUROR:
            if len(self.headcomment_set.all()) != 0:
                return False
            else:
                return True
        else:
            return False


class Vote(models.Model):
    """
    Vote if challenge is deemed successful or not by a juror for a given challenge.
    """
    POSITIVE = "positive"
    NEGATIVE = "negative"
    DECISION_CHOICES = ((POSITIVE, POSITIVE), (NEGATIVE, NEGATIVE))

    decision = models.CharField(max_length=10, choices=DECISION_CHOICES, default="")
    juror = models.OneToOneField(Role) # only use for jurors!

    def __unicode__(self):
        return "{0} vote of {1}".format(self.decision, self.juror)
