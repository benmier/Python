from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^products/', include('apps.products.urls')),
]
