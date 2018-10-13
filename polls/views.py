from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import Question, Choice
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView
from rest_framework.response import Response
from rest_framework import status
from .serializers import QuestionSerializer, ChoiceSerializer
from rest_framework.views import APIView
import json
import subprocess
# Create your views here.
class QuestionList(APIView):

    def get(self, request):
        question = Question.objects.raw('SELECT * FROM polls_question order by id')
        serializer = QuestionSerializer(question, many= True)
        return Response({'latest_question_list':serializer.data}, template_name='index.html')

    def post(self, request):
        serializer = QuestionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChoiceList(APIView):

    def get(self, request):
        choice = Choice.objects.raw('SELECT * FROM polls_choice order by id')
        serializer = ChoiceSerializer(choice, many= True)
        return Response(serializer.data)

    def get_choice(self, request, choice_id):
        choice = Choice.objects.raw('SELECT * FROM polls_choice')
        serializer = ChoiceSerializer(choice, many= True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ChoiceSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        data = Question.objects.raw('SELECT * FROM polls_question order by pub_date limit 5')
        return data


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #redisplay the question voting form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


#get all data from question index
class questionList_es(APIView):
    def get(self, request):
        dumpcmd = """curl -X GET -H 'Content-Type: application/json' "http://localhost:9200/question/_search" -d'{"query": {"match_all": {}}}'"""
        results=json.loads(subprocess.check_output(dumpcmd, shell=True))
        results_list=[]
        for x in results["hits"]["hits"]:
            results_list.append(x['_source'])
        return Response(results_list, status=status.HTTP_201_CREATED)
