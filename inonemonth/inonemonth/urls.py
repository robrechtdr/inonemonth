from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover() # To enable the admin:

from core.views import UserRetrieveAPIView
from challenges.views import (challenge_create_view, invite_jurors_view,
                              challenge_detail_view, ChallengeRetrieveAPIView,
                              RoleRetrieveAPIView)
from comments.views import TailCommentDestroyAPIView
#                            ListCreateAPIView,
#                            CommentRetrieveUpdateDestroyAPIView)

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='home.html'), name="home_view"),
    url(r'^carousel$', TemplateView.as_view(template_name='carousel.html'), name="home_view"),
    url(r'^basic$', TemplateView.as_view(template_name='home2.html')),

    url(r'^accounts/', include('allauth.urls')),

    url(r'^challenge/create/$', challenge_create_view, name="challenge_create_view"),
    url(r'^challenge/(?P<pk>\d+)/invite-jurors/$', invite_jurors_view, name="challenge_invite_jurors_view"),
    url(r'^challenge/(?P<pk>\d+)/detail/$', challenge_detail_view, name="challenge_detail_view"),

    url(r'^api/users/(?P<pk>[0-9]+)/$', UserRetrieveAPIView.as_view(), name="user_api_retrieve"),
    url(r'^api/challenges/(?P<pk>[0-9]+)/$', ChallengeRetrieveAPIView.as_view(), name="challenge_api_retrieve"),
    url(r'^api/roles/(?P<pk>[0-9]+)/$', RoleRetrieveAPIView.as_view(), name="role_api_retrieve"),
    url(r'^api/tail-comments/(?P<pk>[0-9]+)/$', TailCommentDestroyAPIView.as_view(), name="tail_comment_api_destroy"),
    #url(r'^api/comments/$', CommentListCreateAPIView.as_view(), name="comment_api_list_create"),
    #url(r'^api/comments/(?P<pk>[0-9]+)/$', CommentRetrieveUpdateDestroyAPIView.as_view(), name="comment_api_retrieve_update_destroy"),
    url(r'^api-auth/', include('rest_framework.urls', # Enable browseable api
                               namespace='rest_framework')),

    url(r'^admin/', include(admin.site.urls)),
)

########## To serve media files in development ##################################
# See: https://docs.djangoproject.com/en/dev/howto/static-files/#serving-files-uploaded-by-a-user-during-development
# This snippet only has an effect in debug mode:
# https://github.com/django/django/blob/master/django/conf/urls/static.py
from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
################################################################################

########### Sandbox mini view start ################
from django.http import HttpResponse
from django.shortcuts import render

def sandbox_mini(request):
    from allauth.socialaccount.models import SocialLogin, SocialAccount
    from django.contrib.auth import get_user_model

    html = 'Heeey!'
    import pdb; pdb.set_trace()
    return HttpResponse(content=html)
    #return render(request=request, template_name='my_template.html',
    #  dictionary={"message": "Heeeey!"})

urlpatterns += patterns('',
    url(regex=r'sbvm/$', view=sandbox_mini, name="sandbox_mini"),
)
########### Sandbox mini view end ################
