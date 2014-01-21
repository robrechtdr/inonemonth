from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from challenges.views import (challenge_create_view, invite_jurors_view,
    challenge_detail_view, ChallengeDetailView)


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='carousel.html'), name="home_view"),
    url(r'^basic$', TemplateView.as_view(template_name='home.html')),
    #url(r'^$', TemplateView.as_view(template_name='carousel.html'), name="home_view"),

    url(r'^accounts/', include('allauth.urls')),

    url(r'^challenge/create/$', challenge_create_view, name="challenge_create_view"),
    url(r'^challenge/invite-jurors/(?P<pk>\d+)/$', invite_jurors_view, name="challenge_invite_jurors_view"),
    url(r'^challenge/detail/(?P<pk>\d+)/$', ChallengeDetailView.as_view(), name="challenge_detail_view"),
    #url(r'^challenge/detail/(?P<pk>\d+)/$', challenge_detail_view, name="challenge_detail_view"),
    #url(r'^challenge/(?P<username>\w+)/detail/(?P<challenge_id_code>\w+)/$', ChallengeDetailView.as_view(), name="challenge_detail_view"),
    #url(r'^challenge/(?P<username>\w+)/create/', challenge_create_view, name="challenge_create_view"),


    # Examples:
    # url(r'^$', 'inonemonth.views.home', name='home'),
    # url(r'^inonemonth/', include('inonemonth.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
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
