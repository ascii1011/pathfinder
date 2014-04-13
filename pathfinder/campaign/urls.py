from django.conf.urls import patterns, url
from . import models, views 

urlpatterns = patterns('',
    url(r'^$', views.CampaignList.as_view(), name='campaign-list'),
    url(r'^(?P<slug>[\w-]+)/$', views.CampaignDetail.as_view(), name="campaign-detail"),
    url(r'^add/$', views.CampaignList.as_view(), name='campaign-add'),
    url(r'^edit/(?P<slug>[\w-]+)/$', views.CampaignDetail.as_view(), name="campaign-edit"), 
)
