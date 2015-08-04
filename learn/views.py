from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, JsonResponse
from learn.models import Person, Entry, Blog
from django.views.decorators.http import *
from django.views.decorators.gzip import gzip_page
import datetime


def index(request):
    blogs = Blog.objects.all()
    # response = ', '.join(map(unicode, Entry.objects.filter(blog__in=list(blogs))))
    return render(request, template_name='index.html',
                  context={'blogs': blogs}, content_type="text/html")


def get_last_modified(request, *args, **kwargs):
    last_modified_date = None
    if 'blog_id' in kwargs:
        last_modified_date = datetime.datetime.today()

    return last_modified_date


@last_modified(get_last_modified)
@gzip_page
def detail(request, blog_id):
    return HttpResponse("Blog id: %s" % blog_id)


def year(request, *args, **kwargs):
    response = HttpResponse(u"<h1>Year: %(year)s</h1>" % kwargs)
    return response


def month(request, *args, **kwargs):
    return HttpResponse("Year: %(year)s<br>Month: %(month)s" % kwargs)


def day(request, *args, **kwargs):
    return HttpResponse("Year: %(year)s<br>Month: %(month)s<br>Day: %(day)s" % kwargs)


def upload_file(request):
    from learn.forms import UploadFileForm
    from djbook import settings

    if request.method == 'POST':
        print request.FILES
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            if form.cleaned_data['title']:
                filename = settings.os.path.join(settings.MEDIA_ROOT, form.cleaned_data['title'])
            else:
                filename = settings.os.path.join(settings.MEDIA_ROOT, request.FILES['file'].name)
            with open(filename, 'wb+') as new_file:
                for chunk in request.FILES['file'].chunks():
                    new_file.write(chunk)
            return redirect(request.META['HTTP_REFERER'], permanent=True)
    else:
        form = UploadFileForm()

    return render(request, template_name='upload.html', context={
        'form': form,
    })
