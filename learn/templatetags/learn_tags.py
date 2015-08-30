from django import template
from django.utils.formats import mark_safe
from django.utils.html import conditional_escape

register = template.Library()


# Custom filters
@register.filter(name='mark_sub', needs_autoescape=True)
def mark_sub(value, arg, autoescape=True):
    if autoescape:
        escape = conditional_escape
    else:
        escape = lambda x: x
    return mark_safe(value.replace(arg, '<span class="marked">{0}</span>'.format(escape(arg))))


# Custom tags
@register.simple_tag(takes_context=True, name='counter')
def show_counter(context, *args, **kwargs):
    return "Counter: <b>{0}</b>".format(context['counter'])


@register.inclusion_tag(file_name='tags/posts_list.html')
def posts_list():
    from learn.models import Entry

    return {'entries': Entry.objects.all()[:5]}


@register.assignment_tag
def register_var(*args, **kwargs):
    return "some value"
