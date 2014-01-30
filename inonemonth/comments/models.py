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

    def __unicode__(self):

        return "{0} from {1} on {2}".format(#self.type.capitalize(),
                                            self.owner, self.posted_on)


class HeadComment(CommentBase):
   pass


class TailComment(CommentBase):
    head = models.ForeignKey(HeadComment) # The head comment it belongs to
