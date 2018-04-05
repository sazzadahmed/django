
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
#from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^polls/', include('polls.urls',namespace='polls')),
    url(r'^polll1/', include('polll1.urls',namespace='polll1')),
    url(r'^articles/', include('articles.urls',namespace='articles')),
    #url(r'^', include('snippet.urls')),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

