from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from polls.models import Question, Choice
from django.utils import timezone

from django.views import generic


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    queryset = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    template_name = 'polls/detail.html'
    context_object_name = 'question'
    model = Question
    pk_url_kwarg = 'question_id'
    queryset = Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    template_name = 'polls/results.html'
    context_object_name = 'question'
    model = Question
    pk_url_kwarg = 'question_id'


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
