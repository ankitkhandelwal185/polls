# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.

def index(request):
    latest = Question.objects.order_by('-pub_date')[:5]
    #output = ''.join([q.question_text for q in latest
    context = {'latest_question_list': latest}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question Does Not Exist")
    return render(request, 'polls/detail.html', {question: question})

def results(request, question_id):
    response = "You're looking at question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're looking at question %s"%question_id)
