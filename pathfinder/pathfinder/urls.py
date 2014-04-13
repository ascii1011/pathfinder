from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from pathfinder.views import dashboard

urlpatterns = patterns('',
    url(r'^$', dashboard.as_view(), name='home'),
    url(r'^campaign/', include('campaign.urls')),
    #url(r'^source/', include('source.urls')),
    #url(r'^article/', include('article.urls')),
    #url(r'^traceroute/', include('traceroute.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
