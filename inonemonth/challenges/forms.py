# -*- coding: utf-8 -*-

from django import forms
from pagedown.widgets import PagedownWidget

from .models import Challenge

class ChallengeCreateModelForm(forms.ModelForm):
    body = forms.CharField(widget=PagedownWidget(), label="Body")

    class Meta:
        model = Challenge
        fields = ("title", "body")
