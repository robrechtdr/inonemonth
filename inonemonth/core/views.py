import allauth.socialaccount.views
import allauth.account.views

from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from rest_framework import generics

from .serializers import UserSerializer


User = get_user_model()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class JurorChallengeSigninView(allauth.account.views.LoginView):
    template_name = "juror_challenge_signin.html"

    def get_success_url(self):
        return reverse("challenge_detail_view", kwargs={"pk": self.kwargs["pk"]})


class BindEmailView(allauth.socialaccount.views.SignupView):
    template_name = "bind_email.html"
