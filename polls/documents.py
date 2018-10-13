from django_elasticsearch_dsl import DocType, Index,fields
from .models import Question, Choice
#index for Question model
question = Index('question')
question.settings(
	number_of_shards=1,
	number_of_replicas=0
)

@question.doc_type
class questionDocument(DocType):

	class Meta:
		model = Question # The model associated with this DocType
		fields = ['question_text','pub_date']

#index for choice model
choice = Index('choice')
choice.settings(
	number_of_shards=1,
	number_of_replicas=0
)

@choice.doc_type
class choiceDocument(DocType):

	class Meta:
		model = Choice # The model associated with this DocType
		fields = ['choice_text', 'votes']
