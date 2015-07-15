from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^test/', include('learn.urls', namespace='learn')),
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^admin/', include(admin.site.urls)),
]
