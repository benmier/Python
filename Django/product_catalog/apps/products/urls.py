from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show),
    url(r'^(?P<product_id>\d+)', views.edit),
    url(r'^delete/(?P<product_id>\d+)', views.delete),
    url(r'^update/(?P<product_id>\d+)', views.update),
    url(r'^add', views.add),
]