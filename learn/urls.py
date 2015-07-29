from django.conf.urls import url
from learn import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^blog/(?P<blog_id>[0-9]+)/$', views.detail, name='detail'),
]
