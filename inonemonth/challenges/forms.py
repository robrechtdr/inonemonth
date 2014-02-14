# -*- coding: utf-8 -*-

from django import forms
from pagedown.widgets import PagedownWidget

from .models import Challenge
from .validators import RepoExistanceValidator

class ChallengeCreateModelForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(ChallengeCreateModelForm, self).__init__(*args, **kwargs)
        self.fields["repo"].validators.append(RepoExistanceValidator(user))

    body = forms.CharField(widget=PagedownWidget(attrs={"placeholder":"Complete description of my challenge"}), label="Body")
    repo = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"my_repo/my_branch (existing repo on my Github account)"}), label="Repo")

    class Meta:
        model = Challenge
        widgets = {
            "title": forms.TextInput(attrs={"placeholder":
                                            "A one line description of my challenge"}),
        }
        fields = ("title", "body", "repo")


class JurorInviteForm(forms.Form):
    # Strange that with only 1 form in formset, required does not apply
    # without writing it here explicitly.
    email = forms.EmailField(required=True)
