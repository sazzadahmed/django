from django.conf.urls import url
from . import views

urlpatterns = [
	url('^$',views.Te_index,name='index'),
    url('^create/',views.create_Te,name='create_te'),
    url('^update_te/(?P<id>[0-9]+)',views.create_save_data,name='update_te'),
    url('^createfromsave/',views.create_save_data,name='c_s_d'),
    url('^viewdetail/(?P<id>[0-9]+)',views.Te_single,name='show_detail'),
    url('^delete/(?P<id>[0-9]+)',views.delete_data,name='delete'),
    url('^update/(?P<id>[0-9]+)',views.form_update,name='update'),

]