from django.conf.urls import url
from learn import views

urlpatterns = [
    url(r'^$', views.index),
]
