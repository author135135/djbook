from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from polls.models import Question, Choice


def index(request):
    questions = Question.objects.order_by('-pub_date')[:5]
    return render(request, template_name='polls/index.html', context={
        'latest_question_list': questions,
    })


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, template_name='polls/detail.html', context={
        'question': question,
    })


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, template_name="polls/results.html", context={
        'question': question,
    })


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, template_name="polls/detail.html", context={
            'question': question,
            'error_message': "You didn't select a choice."
        })

    choice.votes += 1
    choice.save()

    return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
