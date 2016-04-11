from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^$', include('apps.home.urls')),
    url(r'^ninja/', include('apps.ninja.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
