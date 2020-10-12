from django.urls import path
from .views import SurveyList,SurveyDetailView,QuestionList,QuestionDetailView,AnswerList,AnswerDetailView
urlpatterns = [
    path('', SurveyList.as_view()),
    path('<int:id>', SurveyDetailView.as_view()),
    path('questions', QuestionList.as_view()),
    path('questions/<int:id>', QuestionDetailView.as_view()),
    path('answers', AnswerList.as_view()),
    path('answers/<int:id>', AnswerDetailView.as_view()),
]