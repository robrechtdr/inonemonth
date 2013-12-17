from django.db import models


class Challenge(models.Model):
    # Use placeholder: one line description of what you want to achieve
    title = models.CharField(max_length=200)
    description = models.TextField()
