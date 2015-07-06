from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from polls.models import Question


def index(request):
    questions = Question.objects.order_by('-pub_date')[:5]
    return render(request, template_name='polls/index.html', context={
        'latest_question_list': questions,
    })


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, template_name='polls/detail.html', context={
        'question': question
    })


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
