from rest_framework.serializers import ModelSerializer

from .models import Survey,Questions

class SurveySerializer(ModelSerializer):


    class Meta:
        model=Survey
        fields=['id','survey_title','survey_topic','survey_description','expiry_date','added_date','number_of_questions']

class QuestionSerializer(ModelSerializer):


    class Meta:
        model=Questions
        fields=['id','survey_uid','question_text','mandatory','update_date']

class AnswerSerializer(ModelSerializer):


    class Meta:
        model=Questions
        fields=['id','question_id','user_id','answer']