from django.db import models

from profiles.models import Profile

class Challenge(models.Model):
    # Use placeholder: one line description of what you want to achieve
    title = models.CharField(max_length=200)
    body = models.TextField()
    #srce_control_platform_link/github_link
    #starting_date
    clencher = models.ForeignKey(Profile, related_name="challenge_set_clencher", null=True)
    jurors = models.ManyToManyField(Profile, related_name="challenge_set_jurors", null=True)

