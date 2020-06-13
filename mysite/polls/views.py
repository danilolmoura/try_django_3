from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = 'polls/index.html'

    context = {
        'latest_question_list': latest_question_list,
    }

    return render(request, template, context)

def detail(request, question_id):
    template = 'polls/detail.html'

    question = get_object_or_404(Question, pk=question_id)
    return render(request, template, {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    template = 'polls/results.html'
    return render(request, template, {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    template = 'polls/detail.html'
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        context = {
            'question': question,
            'error_message': "You didn't select a choice.",
        }
        return render(request, template, context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(
            reverse('polls:results', args=(question.id,)))
