from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.http import Http404
from django.urls import reverse
from django.utils import timezone
from itertools import chain

# Create your views here.


def index(request):
    return render(request, 'indexxx.html')


def webindex(request):
    latest_question_list = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list}
    return render(request, 'web/index.html', context)


def student(request, id):
    return HttpResponse(id)


def web(request):
    return HttpResponse('Welcome!')


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question dose not exist')
    return render(request, 'web/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'web/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'web/detail.html', {
            'question': question,
            'error_message': 'you did not select a choice'
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('web:results', args=(question.id,)))
