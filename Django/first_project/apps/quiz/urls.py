from django.conf.urls import patterns, url
from . import views
# for django 1.9 use from . import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^(?P<question_id>\d+)/$', views.show, name='show'),
)