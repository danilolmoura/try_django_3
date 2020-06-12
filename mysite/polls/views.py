from django.shortcuts import get_object_or_404, render

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
   response = "You're looking at the results of question %s."
   return render(request, response)

def vote(request, question_id):
	response = "You're voting on question %s" % question_id
	return render(request, response)

