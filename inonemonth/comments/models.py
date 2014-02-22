from __future__ import absolute_import

from django.db import models
from challenges.models import Role
from challenges.models import Challenge


class CommentBase(models.Model):
    text = models.TextField()
    owner = models.ForeignKey(Role)
    posted_on = models.DateTimeField(auto_now_add=True)
    last_modified_on = models.DateTimeField(auto_now=True)
    challenge = models.ForeignKey(Challenge)

    class Meta:
        abstract = True


class HeadComment(CommentBase):
    pass

    def __unicode__(self):
        return "Head comment from {0} on {1}".format(self.owner, self.posted_on)


class TailComment(CommentBase):
    head = models.ForeignKey(HeadComment) # The head comment it belongs to

    def __unicode__(self):
        return "Tail comment from {0} on {1}".format(self.owner, self.posted_on)
