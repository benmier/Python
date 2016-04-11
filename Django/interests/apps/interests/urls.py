from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^interests$', views.all),
	url(r'^interests/(?P<user_id>\w+)/$', views.one),
]