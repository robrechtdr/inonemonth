from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ChallengeCreateModelForm


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
            return HttpResponseRedirect(reverse_lazy("my_url_name"))
    else:
        form = ChallengeCreateModelForm()

    return render(request=request, template_name='challenge_detail/challenge_create.html',
      dictionary={"form": form})
