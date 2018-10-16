from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.QuestionList.as_view(), name='index'),
    url(r'^choice/$', views.ChoiceList.as_view(), name='choice'),
    #url(r'^choice/(?P<choice_id>[0-9]+)/$', views.ChoiceList.as_view({'choice_id'}), name='get_choice'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^polls/es/$', views.questionList_es.as_view()),
    url(r'^choice/es/$', views.choiceList_es.as_view()),
    url(r'^es/$', views.question_es.as_view()),
]
