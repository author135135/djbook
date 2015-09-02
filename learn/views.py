# coding: utf-8
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse, Http404, JsonResponse
from django.views.decorators.http import *
from django.views.decorators.gzip import gzip_page
from django.views.generic import TemplateView, ListView, DetailView, View
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView, TemplateResponseMixin, ContextMixin
from learn.models import Person, Entry, Blog, Author
from learn.forms import UploadFileForm, ContactForm, NameForm, DivErrorList, BlogForm
import datetime


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


def download_csv(request):
    import csv

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="blogs.csv"'

    blogs = list(Blog.objects.all().values())

    if not blogs:
        return HttpResponse('No blogs found')

    writer = csv.DictWriter(f=response, fieldnames=blogs[0].keys())
    writer.writeheader()
    for blog in blogs:
        for k, v in blog.iteritems():
            if type(v) is unicode:
                blog[k] = v.encode('utf-8')
        writer.writerow(blog)

    return response


def download_csv_txt(request):
    from django.shortcuts import render

    blogs = list(Blog.objects.all().values())

    if not blogs:
        return HttpResponse('No blogs found')

    for blog in blogs:
        for k, v in blog.iteritems():
            if type(v) is unicode:
                blog[k] = v.encode('utf-8')

    response = render(request, template_name='csv_template.txt', context={
        'head_row': ','.join(blogs[0].keys()),
        'rows': blogs
    })

    response['Content-Type'] = 'text/csv'
    response['Content-Disposition'] = 'attachment; filename="blogs.csv"'

    return response


# Generate pdf
def pdfview(request):
    from reportlab.pdfgen import canvas

    response = HttpResponse(content_type='application/pdf')

    c = canvas.Canvas(response, bottomup=False)
    t = c.beginText(100, 100)
    t.textLine("Blogs")

    c.drawText(t)

    c.showPage()
    c.save()

    return response


# Static page view

class StaticPageView(TemplateResponseMixin, ContextMixin, View):
    template_name = 'static_page.html'

    def get_context_data(self, **kwargs):
        from django.utils.lorem_ipsum import paragraphs

        context = super(StaticPageView, self).get_context_data(**kwargs)
        context['static_text'] = paragraphs(10)

        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        return self.render_to_response(context)


class TestManyDataMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TestManyDataMixin, self).get_context_data(**kwargs)
        context['many_data_mixin'] = 'value'

        return context


class EntryListView(TestManyDataMixin, ListView):
    template_name = 'index.html'
    queryset = Entry.objects.all().prefetch_related('authors')
    context_object_name = 'entries'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)
        context['date'] = datetime.datetime.now().date()

        return context


class BlogDetailView(TestManyDataMixin, DetailView):
    model = Author
    template_name = 'blog_detail.html'
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['blogs'] = Blog.objects.filter(entry__authors=self.object).distinct()
        context['entries'] = Entry.objects.filter(authors=self.object)[:5]

        return context


# Contact form CBV
class ContactView(FormView):
    template_name = 'contacts.html'
    form_class = ContactForm
    success_url = '/test/'

    def form_valid(self, form):
        form.send()

        return super(ContactView, self).form_valid(form)


# CBV to model Blog
class TestMixin(object):
    def get_object(self, queryset=None):
        obj = super(TestMixin, self).get_object(queryset)
        print obj
        return obj


class CreateBlogView(CreateView):
    model = Blog
    template_name = 'blog_create.html'
    success_url = '/test/'

    def get_form(self, form_class=None):
        if form_class is None:
            from django import forms

            form_class = forms.modelform_factory(self.model, fields='__all__', exclude=['image'])
        return super(CreateView, self).get_form(form_class)

    def get_form_kwargs(self):
        kwargs = super(CreateBlogView, self).get_form_kwargs()
        kwargs['error_class'] = DivErrorList
        return kwargs


class EditBlogView(UpdateView):
    model = Blog
    fields = ['name', 'tagline', 'image']
    template_name = 'blog_edit.html'
    success_url = '/test/'


class DeleteBlogView(DeleteView):
    model = Blog
    success_url = '/test/'
    template_name = 'blog_delete.html'


class UploadFormView(FormView):
    template_name = 'upload_form.html'
    form_class = UploadFileForm

    def form_valid(self, form):
        from django.core.urlresolvers import reverse
        from djbook import settings

        self.success_url = reverse('learn:upload-form')

        if form.cleaned_data['title']:
            filename = settings.os.path.join(settings.MEDIA_ROOT, form.cleaned_data['title'])
        else:
            filename = settings.os.path.join(settings.MEDIA_ROOT, self.request.FILES['file'].name)

        with open(filename, 'wb+') as new_file:
            for chunk in self.request.FILES['file'].chunks():
                new_file.write(chunk)

        return super(UploadFormView, self).form_valid(form)


class FormsTestView(SuccessMessageMixin, FormView):
    template_name = 'forms-test.html'
    form_class = NameForm
    success_message = 'Form success'

    def form_valid(self, form):
        from django.core.urlresolvers import reverse

        self.success_url = reverse('learn:forms_test')
        return super(FormsTestView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(FormsTestView, self).get_form_kwargs()
        kwargs['auto_id'] = False
        kwargs['error_class'] = DivErrorList
        return kwargs
