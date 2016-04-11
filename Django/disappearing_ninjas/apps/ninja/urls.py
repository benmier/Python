from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^(?P<ninja_color>\w+)/$', views.index),
]
