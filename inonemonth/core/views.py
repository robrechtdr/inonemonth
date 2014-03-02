from __future__ import absolute_import

import allauth.socialaccount.views
import allauth.account.views

from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from rest_framework import generics

from .serializers import UserSerializer
from challenges.decorators import auth_user_has_github_account


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


class ConfirmEmailView(allauth.account.views.ConfirmEmailView):
    def get_template_names(self):
        if self.request.method == 'POST':
            return ["email_confirmed.html"]
        else:
            return ["email_confirm.html"]


class ConnectionsView(allauth.socialaccount.views.ConnectionsView):
    template_name = "bind_github.html"

connections = login_required(ConnectionsView.as_view())


class LogoutView(allauth.account.views.LogoutView):
    template_name = "logout.html"

logout = LogoutView.as_view()


class LoginView(allauth.account.views.LoginView):
    template_name = "login.html"

login = LoginView.as_view()


class GithubSigninView(allauth.account.views.LoginView):
    template_name = "github_signin.html"

github_signin = auth_user_has_github_account(GithubSigninView.as_view())
