from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='home.html')),

    # Examples:
    # url(r'^$', 'inonemonth.views.home', name='home'),
    # url(r'^inonemonth/', include('inonemonth.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

########### Sandbox mini view start ################
from django.http import HttpResponse
from django.shortcuts import render

def sandbox_mini(request):
    raise Error
    html = 'Heeey!'
    return HttpResponse(content=html)
    #return render(request=request, template_name='my_template.html',
    #  dictionary={"message": "Heeeey!"})

urlpatterns += patterns('',
    url(regex=r'sbm/$', view=sandbox_mini, name="sandbox_mini"),
)
########### Sandbox mini view end ################
