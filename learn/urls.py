from django.conf.urls import url
from learn import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'blog/upload/$', views.upload_file),
    url(r'^blog/(?P<year>[0-9]{4})/$', views.year),
    url(r'^blog/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month),
    url(r'^blog/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.day),
    url(r'^blog/(?P<blog_id>[0-9]+)/$', views.detail, name='detail'),
]
