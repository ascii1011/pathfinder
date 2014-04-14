from django.conf.urls import patterns, url
from . import views 

urlpatterns = patterns('',
    url(r'^$', views.CampaignList.as_view(), name='campaign-list'),
    url(r'^add/$', views.CampaignCreate.as_view(), name='campaign-add'),
    url(r'^(?P<slug>[\w-]+)/$', views.CampaignDetail.as_view(), name="campaign-detail"),
    url(r'^edit/(?P<slug>[\w-]+)/$', views.CampaignUpdate.as_view(), name="campaign-edit"), 
)
