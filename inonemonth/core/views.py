from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from allauth.account.views import LoginView
from rest_framework import generics

from .serializers import UserSerializer


User = get_user_model()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class JurorChallengeSigninView(LoginView):
    template_name = "juror_challenge_signin.html"

    def get_success_url(self):
        return reverse("challenge_detail_view", kwargs={"pk": self.kwargs["pk"]})
