from django.conf.urls import patterns, url
from . import views 

urlpatterns = patterns('',
    url(r'^$', views.SourceList.as_view(), name='source-list'),
    url(r'^add/$', views.SourceCreate.as_view(), name='source-add'),
    url(r'^(?P<slug>[\w-]+)/$', views.SourceDetail.as_view(), name="source-detail"),
    url(r'^edit/(?P<slug>[\w-]+)/$', views.SourceUpdate.as_view(), name="source-edit"), 
)
