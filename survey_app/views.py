from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Survey, Questions, Answer
from .serializers import SurveySerializer,QuestionSerializer,AnswerSerializer
from rest_framework import permissions
from rest_framework import viewsets


class SurveyList(ListCreateAPIView):

    serializer_class = SurveySerializer
    permission_classes = (permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Survey.objects.filter(owner=self.request.user)

class SurveyDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = SurveySerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'

    def get_queryset(self):
        return Survey.objects.filter()

class QuestionList(ListCreateAPIView):

    serializer_class = QuestionSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Questions.objects.filter()

class QuestionDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = QuestionSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'

    def get_queryset(self):
        return Questions.objects.filter()

class AnswerList(ListCreateAPIView):

    serializer_class = AnswerSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Answer.objects.filter()

class AnswerDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = AnswerSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'

    def get_queryset(self):
        return Answer.objects.filter()