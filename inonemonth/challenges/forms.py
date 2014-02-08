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
    # Strange that with only 1 form in formset, required does not apply
    # without writing it here explicitly.
    email = forms.EmailField(required=True)
