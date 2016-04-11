from django.conf.urls import patterns, url
from . import views
# for django 1.9 use from . import views
urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
)