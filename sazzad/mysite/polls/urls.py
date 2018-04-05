from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^create/',views.create,name='create'),
    url(r'^view/(?P<pk>[0-9]+)$',views.view,name='view'),
    url(r'^update/(?P<pk>[0-9]+)$',views.update,name='update'),
    url(r'^delete/(?P<pk>\d+)$',views.delete,name='delete'),
    url(r'^createview/',views.QuestionListView.as_view(),name='createview'),
    url(r'^updateview/(?P<pk>\d+)$',views.EditQuestionView.as_view(),name='updateview'),
    url(r'^detailview/(?P<pk>\d+)$',views.QuestinDetailView.as_view(),name='detailview'),
    url(r'^deleteview/(?P<pk>\d+)$',views.QuestionDeleteView.as_view(),name='deleteview'),
    url(r'^createpublisher/',views.PublisherCreateView.as_view(),name='publishcreate'),
    url(r'^updatepublisher/(?P<pk>[0-9]+)$',views.PublisherUpdateView.as_view(),name='publishupdate'),
    url(r'^deletepublisher/(?P<pk>[0-9]+)$',views.PublisherDeleteView.as_view(),name='publishdelete'),
    url(r'^listpublisher/$',views.PublishListView.as_view(),name='listpublisher'),
    url(r'^formcheck/$',views.Contant.as_view(),name='formcheck'),
    url(r'^formtest$',views.formsettest,name='formtest'),
    url(r'^formtesttest$',views.saveMyspecialFuction,name='formtesttest'),



]
