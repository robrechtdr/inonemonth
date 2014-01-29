from django.db import models
from challenges.models import Role


class Comment(models.Model):
    HEAD = "head"
    TAIL = "tail"
    COMMENT_CHOICES = ((HEAD, HEAD.capitalize()), (TAIL, TAIL.capitalize()))

    text = models.TextField()
    # Only Jurors should be allowed to make a Head comment, check with js
    type = models.CharField(max_length=10, choices=COMMENT_CHOICES)
    # The comment it belongs to
    head = models.ForeignKey("self")
    owner = models.ForeignKey(Role)
    posted_on = models.DateTimeField(auto_now_add=True)
    last_modified_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "{0} from {1} on {2}".format(self.type.capitalize(),
                                            self.owner, self.posted_on)
