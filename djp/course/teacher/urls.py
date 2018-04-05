
from django.conf.urls import url,include
from . import view1,views

urlpatterns = [
    url(r'^create$',view1.TeacherCreateView.as_view(),name='create'),
    url(r'^formsubmit',views.formdata,name='formdata'),
    url(r'^singleview/(?P<id>[0-9]+)',views.single_view,name='singleview'),
    url(r'^update/(?P<pk>[0-9]+)',view1.TeacherUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>[0-9]+)',view1.TeacherDeleteView.as_view(),name='delete'),
    url(r'^updateform/(?P<id>[0-9]+)',views.formdata_update,name='updateform'),
    url(r'^$',view1.TeacherListView.as_view(),name='index1'),
    url(r'^showteacherdetail/(?P<pk>[0-9]+)$',view1.TeacherDetailView.as_view(),name='detail'),
]
