from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from learn.models import Person


def index(request):
    response = Person.objects.get(pk=1)
    return HttpResponse(response)
