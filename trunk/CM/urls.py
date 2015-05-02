from django.conf.urls import patterns, include, url
from django.contrib import admin
from .settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CM.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include('principal.urls')),
    url(r'^admin/', include(admin.site.urls)),
)+ static(MEDIA_URL, document_root=MEDIA_ROOT)
