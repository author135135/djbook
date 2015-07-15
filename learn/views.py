from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from learn.models import Person


def index(request):
    person = get_object_or_404(Person, pk=1)
    return HttpResponse(person)
