from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import DetailView

from .forms import ChallengeCreateModelForm
from .models import Challenge

def challenge_create_view(request):
    if request.method == "POST":
        form = ChallengeCreateModelForm(request.POST)
        if form.is_valid():
            # pre processing

            model = form.instance.__class__
            cleaned_dic = form.cleaned_data
            #cleaned_dic.pop(field_name)  # If frm field not def in model
            inst = model.objects.create(**cleaned_dic)
            inst.save()

            # post processing
            return HttpResponseRedirect(reverse_lazy("challenge_detail_view", kwargs={"pk": inst.pk}))
    else:
        form = ChallengeCreateModelForm()

    return render(request=request, template_name='challenge/challenge_create.html',
      dictionary={"form": form})


class ChallengeDetailView(DetailView):
    template_name = "challenge/challenge_detail.html"
    model = Challenge
    context_object_name = "model"
