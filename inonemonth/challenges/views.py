from __future__ import absolute_import

from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test, login_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import DetailView
from django.forms.formsets import formset_factory

from rest_framework import generics

from core.models import UserExtension
from core.forms import RequiredFormSet
#from core.allauth_utils import create_allauth_user, generate_password
#from core.mail_utils import send_invitation_mail_to_juror
from comments.forms import HeadCommentForm, TailCommentForm
from comments.models import HeadComment, TailComment
from .forms import ChallengeCreateModelForm, JurorInviteForm
from .models import Challenge, Role, Vote
from .serializers import ChallengeSerializer, RoleSerializer
from .github_utils import get_last_commit_on_branch
from .decorators import auth_user_has_github_account
from core.mail_utils import build_url_base
from .tasks import invite_juror


User = get_user_model()


@login_required(login_url=reverse_lazy("github_signin"))
@auth_user_has_github_account
def challenge_create_view(request):
    if request.method == "POST":
        form = ChallengeCreateModelForm(request.user, data=request.POST)
        if form.is_valid():
            instance = form.save()
            clencher = Role.objects.create(user=request.user,
                                           challenge=instance,
                                           type=Role.CLENCHER)
            # Save start commit
            github_social_account = clencher.user.socialaccount_set.get(id=1)
            github_login = github_social_account.extra_data["login"]
            instance.start_commit = get_last_commit_on_branch(github_login,
                                                              instance.repo_name,
                                                              instance.branch_name)
            instance.save()
            return HttpResponseRedirect(reverse_lazy("challenge_invite_jurors_view",
                                        kwargs={"pk": instance.pk}))
    else:
        form = ChallengeCreateModelForm(request.user)

    return render(request=request, template_name='challenge/challenge_create.html',
                  dictionary={"form": form})


@login_required(login_url=reverse_lazy("github_signin"))
@auth_user_has_github_account
def invite_jurors_view(request, **kwargs):
    challenge = Challenge.objects.get(pk=kwargs["pk"])
    # Try to implement this via decorator
    # In case any authenticated user but the clencher to this page visits the
    # page.
    if request.user != challenge.get_clencher().user:
        return HttpResponseRedirect(reverse_lazy("challenge_create_view"))
    # Also bar revisiting this page as a clencher after already having
    # invited jurors?
    JurorInviteFormset = formset_factory(JurorInviteForm, RequiredFormSet)
    if request.method == "POST":
        formset = JurorInviteFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                email = form.cleaned_data["email"]
                url_base = build_url_base(request)
                # Invite jurors via celery queue
                invite_juror.delay(email, challenge, url_base)

            return HttpResponseRedirect(reverse_lazy("challenge_detail_view",
                                        kwargs={"pk": challenge.pk}))
    else:
        formset = JurorInviteFormset()

    return render(request=request, template_name='challenge/detail/invite_jurors.html',
                  dictionary={"formset": formset, "challenge": challenge})


def challenge_detail_view(request, **kwargs):
    challenge = Challenge.objects.get(pk=kwargs["pk"])
    # Should try to do check with decorator, but how to
    # pass the pk of challenge url to it?
    if not challenge.user_has_role(request.user):
        return HttpResponseRedirect(reverse_lazy("challenge_detail_403",
                                                 kwargs={"pk": challenge.pk}))

    role = request.user.role_set.get(challenge=challenge)
    role_api_url = role.get_absolute_url()

    if request.method == "POST":
        head_comment_form = HeadCommentForm(request.POST)
        tail_comment_form = TailCommentForm(request.POST)

        # http://stackoverflow.com/questions/1395807/proper-way-to-handle-multiple-forms-on-one-page-in-django
        # http://stackoverflow.com/questions/866272/how-can-i-build-multiple-submit-buttons-django-form
        if "head-submit" in (head_comment_form.data or tail_comment_form.data):
            if head_comment_form.is_valid() and not challenge.has_ended():
                head_comment_id = head_comment_form.data["id"]
                # In case of comment edit
                if head_comment_id:
                    # Check should be made if the head_comment is owned by the
                    # role
                    head_comment = HeadComment.objects.get(id=head_comment_id)
                    if head_comment.owner == role:
                        head_comment.challenge = challenge
                        head_comment.text = head_comment_form.cleaned_data["text"]
                        head_comment.save()

                        vote = Vote.objects.get(juror=role)
                        vote.decision = head_comment_form.cleaned_data["decision"]
                        vote.save()
                    else:
                        return HttpResponseForbidden()

                else:
                    HeadComment.objects.create(owner=role, challenge=challenge,
                                       text=head_comment_form.cleaned_data["text"])

                    Vote.objects.create(juror=role,
                                   decision=head_comment_form.cleaned_data["decision"])


        elif "tail-submit" in (head_comment_form.data or tail_comment_form.data):
            if tail_comment_form.is_valid() and not challenge.has_ended():
                tail_comment_id = tail_comment_form.data["id"]
                # In case of comment edit
                if tail_comment_id:
                    tail_comment = TailComment.objects.get(id=tail_comment_id)
                    if tail_comment.owner == role:
                        tail_comment.challenge = challenge
                        tail_comment.text = tail_comment_form.cleaned_data["text"]
                        tail_comment.head = HeadComment.objects.get(id=int(tail_comment_form.data["head-id"]))
                        tail_comment.save()
                    else:
                        return HttpResponseForbidden()

                else:
                    TailComment.objects.create(owner=role, challenge=challenge,
                                           text=tail_comment_form.cleaned_data["text"],
                                           head=HeadComment.objects.get(id=int(tail_comment_form.data["head-id"])))

    else:
        head_comment_form = HeadCommentForm()
        tail_comment_form = TailCommentForm()

    return render(request=request, template_name='challenge/detail/challenge_detail.html',
                  dictionary={"role_api_url": role_api_url,
                              "user_role": role,
                              "challenge": challenge,
                              "head_comment_form": head_comment_form,
                              "tail_comment_form": tail_comment_form
                              }
    )


def challenge_detail_403_view(request, **kwargs):
    return render(request=request, template_name='challenge_detail_403.html',
                  status=403)


class ChallengeRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer


class RoleRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
