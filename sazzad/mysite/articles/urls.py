from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', admin.site.urls,name='index'),
    url(r'^create/$',views.ArticlesCreateView.as_view(),name='create'),
    url(r'^list/$',views.ArticlesListView.as_view(),name='list'),
    url(r'^(?P<pk>[0-9]+)$',views.ArticlesDetailView.as_view(),name='detail'),
    url(r'^update/(?P<pk>[0-9]+)$',views.ArticleUpdateView.as_view(),name='update'),
	url(r'^delete/(?P<pk>[0-9]+)$',views.ArticleDeleteView.as_view(),name='delete'),



]