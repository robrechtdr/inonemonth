from __future__ import absolute_import

from django import forms
from pagedown.widgets import PagedownWidget
from challenges.models import Vote


class HeadCommentForm(forms.ModelForm):
    text = forms.CharField(widget=PagedownWidget(),
                           label="Text")
    class Meta:
        model = Vote
        fields = ("text", "decision")


class TailCommentForm(forms.Form):
    text = forms.CharField(widget=PagedownWidget(),
                           label="Text")
