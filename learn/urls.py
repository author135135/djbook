from django.conf.urls import url, include
from learn import views

blogpatterns = [
    url(r'^upload/$', views.UploadFormView.as_view(), name='upload-form'),
    url(r'^static-page/$', views.StaticPageView.as_view()),
    url(r'^(?P<year>[0-9]{4})/$', views.year),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.day),
    url(r'create/$', views.CreateBlogView.as_view(), name='create'),
    url(r'edit/(?P<pk>[0-9]+)/$', views.EditBlogView.as_view(), name='edit'),
    url(r'delete/(?P<pk>[0-9]+)/', views.DeleteBlogView.as_view(), name='delete'),
    url(r'^(?P<pk>[0-9]+)/$', views.BlogDetailView.as_view(), name='detail'),
    url(r'^contacts/$', views.ContactView.as_view(), name='contacts'),
    url(r'^download/$', views.download_csv_txt, name='download'),
    url(r'^pdfview/$', views.pdfview, name='pdfview'),
]

urlpatterns = [
    url(r'^$', views.EntryListView.as_view(), name='index'),
    url(r'^page/(?P<page>[0-9]+)/$', views.EntryListView.as_view(), name='paginate'),
    url(r'^blog/', include(blogpatterns)),
    url(r'^forms-test/$', views.FormsTestView.as_view(), name='forms_test'),
]
