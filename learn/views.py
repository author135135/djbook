from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from learn.models import Person, Entry, Blog


def index(request):
    blogs = Blog.objects.values_list('pk', flat=True)
    response = ', '.join(map(unicode, Entry.objects.filter(blog__in=list(blogs))))
    return render(request, template_name='index.html', context={
        'response': response,
    })

def detail(request, blog_id):
    return HttpResponse("Blog id: %s" % blog_id)
