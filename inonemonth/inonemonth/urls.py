from __future__ import absolute_import

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()  # To enable the admin:

from core.views import (UserRetrieveAPIView, JurorChallengeSigninView,
                        BindEmailView, ConfirmEmailView, connections,
                        logout, login, github_signin)
from challenges.views import (challenge_create_view, invite_jurors_view,
                              challenge_detail_view, ChallengeRetrieveAPIView,
                              RoleRetrieveAPIView, challenge_detail_403_view)
from comments.views import TailCommentDestroyAPIView


urlpatterns = patterns(
    '',
    url(r'^$',
        TemplateView.as_view(template_name='home.html'),
        name="home_view"),
    url(r'^glossary/$',
        TemplateView.as_view(template_name='glossary.html'),
        name="glossary"),


    # How to customize allauth based url? Would need to create
    # a URL setting for Allauth
    url(r'^accounts/social/signup/$',
        BindEmailView.as_view(),
        name="socialaccount_signup"),
    url(r'^accounts/confirm-email/$',
        TemplateView.as_view(template_name="verification_sent.html"),
        name="verification_sent"),
    url(r'^accounts/confirm-email/(?P<key>\w+)/$',
        ConfirmEmailView.as_view(),
        name="confirm_email"),
    url(r'^accounts/social/connections/$',
        connections,
        name="socialaccount_connections"),
    url(r'^accounts/logout/$',
        logout,
        name="account_logout"),
    url(r"^accounts/login/$",
        login,
        name="account_login"),
    # Can set with custom url:
    url(r'^accounts/signin-github/$',
        github_signin,
        name="github_signin"),
    url(r'^accounts/signin-juror/challenges/(?P<pk>\d+)/$',
        JurorChallengeSigninView.as_view(),
        name="juror_challenge_signin"),

    url(r'^accounts/', include('allauth.urls')),


    url(r'^challenges/create/$',
        challenge_create_view,
        name="challenge_create_view"),
    url(r'^challenges/(?P<pk>\d+)/invite-jurors/$',
        invite_jurors_view,
        name="challenge_invite_jurors_view"),
    url(r'^challenges/(?P<pk>\d+)/detail/$',
        challenge_detail_view,
        name="challenge_detail_view"),
    url(r'^challenges/(?P<pk>\d+)/detail/403/$',
        challenge_detail_403_view,
        name="challenge_detail_403"),


    url(r'^api/users/(?P<pk>[0-9]+)/$',
        UserRetrieveAPIView.as_view(),
        name="user_api_retrieve"),
    url(r'^api/challenges/(?P<pk>[0-9]+)/$',
        ChallengeRetrieveAPIView.as_view(),
        name="challenge_api_retrieve"),
    url(r'^api/roles/(?P<pk>[0-9]+)/$',
        RoleRetrieveAPIView.as_view(),
        name="role_api_retrieve"),
    url(r'^api/tail-comments/(?P<pk>[0-9]+)/$',
        TailCommentDestroyAPIView.as_view(),
        name="tail_comment_api_destroy"),
    url(r'^api-auth/', include('rest_framework.urls',  # Enable browseable api
                               namespace='rest_framework')),

    url(r'^admin/', include(admin.site.urls)),
)

########## To serve media files in development ################################
# See: https://docs.djangoproject.com/en/dev/howto/static-files
# /#serving-files-uploaded-by-a-user-during-development
# This snippet only has an effect in debug mode:
# https://github.com/django/django/blob/master/django/conf/urls/static.py
from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
##############################################################################
