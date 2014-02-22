# -*- coding: utf-8 -*-

from __future__ import absolute_import

from django import forms
from pagedown.widgets import PagedownWidget

from .models import Challenge
from .validators import RepoExistanceValidator
from .github_utils import get_repo_and_branch_from_repo_path

class ChallengeCreateModelForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(ChallengeCreateModelForm, self).__init__(*args, **kwargs)
        self.fields["repo"].validators.append(RepoExistanceValidator(user))

    body = forms.CharField(widget=PagedownWidget(attrs={"placeholder":"Complete description of my challenge"}), label="Body")
    repo = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"my_repo/my_branch (existing repo on my Github account)"}), label="Repo")

    def save(self, *args, **kwargs):
        model = self.instance
        repo_path = self.cleaned_data["repo"]
        repo, branch = get_repo_and_branch_from_repo_path(repo_path)
        model.repo_name = repo
        model.branch_name = branch
        model.save()
        return super(ChallengeCreateModelForm, self).save(*args, **kwargs)

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
