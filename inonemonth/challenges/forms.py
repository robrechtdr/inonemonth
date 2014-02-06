# -*- coding: utf-8 -*-

from django import forms
from pagedown.widgets import PagedownWidget

from .models import Challenge

class ChallengeCreateModelForm(forms.ModelForm):
    body = forms.CharField(widget=PagedownWidget(attrs={"placeholder":"Complete description of my challenge"}), label="Body")

    class Meta:
        model = Challenge
        widgets = {
            "title": forms.TextInput(attrs={"placeholder":
                                            "A one line description of my challenge"}),
        }
        fields = ("title", "body")


class JurorInviteForm(forms.Form):
    email = forms.EmailField()
