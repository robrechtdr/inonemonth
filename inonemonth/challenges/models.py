from django.db import models

from profiles.models import Profile

class Challenge(models.Model):
    # Use placeholder: one line description of what you want to achieve
    title = models.CharField(max_length=200)
    description = models.TextField()
    lincoln = models.ForeignKey(Profile, related_name="challenge_set_lincoln", null=True)
    judges = models.ManyToManyField(Profile, related_name="challenge_set_judges", null=True)
