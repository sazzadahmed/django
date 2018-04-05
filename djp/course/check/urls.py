from django.conf.urls import url
from . import views

urlpatterns = [
	 url(r'^$',views.index,name='index'),
	 url(r'^create$',views.createformclass,name='createform'),
	 url(r'^createsubmit$',views.create_form_data_save,name='create'),
	 url(r'^singleview/(?P<id>[0-9]+)$',views.single_document_shortcut,name='singleview'),
	 url(r'^update/(?P<id>[0-9]+)$',views.update,name='update'),
	 url(r'^updateform/(?P<id>[0-9]+)$',views.updateform,name='updateform'),
	 url(r'^deletedata/(?P<id>[0-9]+)$',views.deletedata,name='delete'),


]