from django.conf.urls import patterns, url
from . import views 

urlpatterns = patterns('',
    url(r'^$', views.ArticleList.as_view(), name='article-list'),
    url(r'^add/$', views.ArticleCreate.as_view(), name='article-add'),
    url(r'^(?P<slug>[\w-]+)/$', views.ArticleDetail.as_view(), name="article-detail"),
    url(r'^edit/(?P<slug>[\w-]+)/$', views.ArticleUpdate.as_view(), name="article-edit"), 
)
