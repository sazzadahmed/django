
from django.conf.urls import url,include
from . import views
from rest_framework.routers import DefaultRouter

##router.register(r'snippet',views.SnipperViewset)
urlpatterns = [
    #url(r'^',include(router.urls)),
    #url(r'snippet/(?P<pk>[0-9]+)$',views.snippet_detail)
]
