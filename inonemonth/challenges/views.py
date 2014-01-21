from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import DetailView
from django.forms.formsets import formset_factory

from core.allauth_utils import create_allauth_user
from .forms import ChallengeCreateModelForm, JurorInviteForm
from .models import Challenge
#!! from .decorators import user_has_profile


#!! @user_has_profile
def challenge_create_view(request):
    if request.method == "POST":
        form = ChallengeCreateModelForm(request.POST)
        if form.is_valid():
            # Get Profile based on username
            #!! profile = Profile.objects.get(user=request.user)

            # Save data to challenge
            model = form.instance.__class__
            cleaned_dic = form.cleaned_data
            inst = model.objects.create(**cleaned_dic)
            #!! inst = model.objects.create(clencher=profile, **cleaned_dic)
            # If Juror selection here done then also add jurors to model here.
            inst.save()
            #import pdb; pdb.set_trace()

            #return HttpResponseRedirect(reverse_lazy("challenge_detail_view",
            #                            kwargs={"pk": inst.pk}))
            return HttpResponseRedirect(reverse_lazy("challenge_invite_jurors_view",
                                        kwargs={"pk": inst.pk}))
    else:
        form = ChallengeCreateModelForm()

    return render(request=request, template_name='challenge/challenge_create.html',
                  dictionary={"form": form})


def invite_jurors_view(request, **kwargs):
    JurorInviteFormset = formset_factory(JurorInviteForm)
    challenge = Challenge.objects.get(pk=kwargs["pk"])
    if request.method == "POST":
        formset = JurorInviteFormset(request.POST)
        if formset.is_valid():
            # pre processing

            for form in formset:
                user = create_allauth_user(email=form.cleaned_data["email"])
                # Here, Send invitation email to user to challenge (probably need to
                # deactivate mailing email confirmation)

            """
            model = form.instance.__class__
            #cleaned_dic.pop(field_name)  # If frm field not def in model
            inst = model.objects.create(**cleaned_dic)
            inst.save()
            """

            # post processing
            return HttpResponseRedirect(reverse_lazy("challenge_detail_view",
                                        kwargs={"pk": challenge.pk}))
    else:
        formset = JurorInviteFormset()

    return render(request=request, template_name='challenge/invite_jurors.html',
                  dictionary={"formset": formset, "model": challenge})


class ChallengeDetailView(DetailView):
    template_name = "challenge/challenge_detail.html"
    model = Challenge
    context_object_name = "model"


class challenge_detail_view():
    pass

'''
class detail_view(request, challenge_id_code):
    model = Challenge
    inst = model.objects.get()
    #decode_to_id(challenge_id_code)

    return render(request=request, template_name='challenge/challenge_detail.html',
      dictionary={"model": })
'''
