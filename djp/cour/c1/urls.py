from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.C1_E_ListView.as_view(),name='index'),
    url(r'^create$',views.C1_E_CreateView.as_view(),name='create'),
    url(r'^detail/(?P<pk>[0-9]+)',views.C1_E_Delete.as_view(),name='delete'),
    url(r'^update/(?P<pk>[0-9]+)',views.C1_E_Update.as_view(),name='update'),
    url(r'^view/(?P<pk>[0-9]+)',views.C1_E_View.as_view(),name='view'),

    

]