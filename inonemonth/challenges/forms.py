# -*- coding: utf-8 -*-

from django import forms
from pagedown.widgets import PagedownWidget

from .models import Challenge

class ChallengeCreateModelForm(forms.ModelForm):
    description = forms.CharField(widget=PagedownWidget(), label="Description")

    class Meta:
        model = Challenge
        fields = ("title", "description")
