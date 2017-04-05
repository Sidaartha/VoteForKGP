from django.shortcuts import render, get_object_or_404,render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Question,Choice
from django.template import loader, RequestContext
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def feedback(request):
	return render(request, 'polls/feedback.html')

def index(request):
	latest_questions=Question.objects.order_by('pub_date')[:10]
	return render(request, 'polls/index.html', {'latest_questions':latest_questions})


def detail(request, question_id):
	question=get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question':question })

def results(request, question_id):
	latest_questions=Question.objects.order_by('pub_date')[:10]
	question=get_object_or_404(Question, pk=3)
	name=['Vice President','G.Sec So-Cult','G.Sec Tech','G.Sec Sports']
	return render(request, 'polls/results.html',  {'latest_questions':latest_questions, 'question':question, 'name0':name[0], 'name1':name[1], 'name2':name[2], 'name3':name[3]})
@csrf_exempt
def vote(request, question_id):
	question=get_object_or_404(Question, pk=question_id)
	try:
		selected_choice=question.choice_set.get(pk=request.POST['choice'])
	except:
		return render(request, 'polls/detail.html', {'question':question, 'error_message':'Please select a choice'})
	else:
		question.total_votes+=1
		selected_choice.votes +=1
		print question.total_votes
		print selected_choice.votes



		selected_choice.percentage=(selected_choice.votes)*100/(question.total_votes)
		
		print selected_choice.percentage
		print selected_choice.choice_text
		selected_choice.save()
		question.save()
		ps=Choice.objects.filter(question = question_id)
		for i in ps:
			i.percentage=(i.votes)*100/(question.total_votes)
			i.save()
		question.id +=1
		if question.id > 6:
			return HttpResponseRedirect(reverse('polls:results', args=(3,)))
		else:	
			return render_to_response('polls/detail.html', {'question' : question , 'choice_text' : selected_choice.choice_text})


