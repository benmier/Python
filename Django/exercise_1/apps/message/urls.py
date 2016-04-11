from django.conf.urls import url
from .views import MyView

urlpatterns = [
    url(r'^$', MyView.as_view()),
]
