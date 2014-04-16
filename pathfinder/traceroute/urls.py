from django.conf.urls import patterns, url
from . import views 

urlpatterns = patterns('',
    url(r'^$', views.TracerouteList.as_view(), name='traceroute-list'),
    url(r'^add/$', views.TracerouteCreate.as_view(), name='traceroute-add'),
    url(r'^(?P<slug>[\w-]+)/$', views.TracerouteDetail.as_view(), name="traceroute-detail"),
    url(r'^edit/(?P<slug>[\w-]+)/$', views.TracerouteUpdate.as_view(), name="traceroute-edit"), 
)
