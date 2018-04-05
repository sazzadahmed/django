from django.conf.urls import url
from . import views
urlpatterns = [
    
    url('^$',views.index,name='index'),
    url('^booklist/',views.BookListView.as_view(),name='listbook'),
    url('^detail/(?P<pk>[0-9]+)',views.BookDetailView.as_view(),name='detail_book'),
]