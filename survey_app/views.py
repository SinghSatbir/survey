from django.http import HttpResponse
from django.shortcuts import render
from PIL import Image
# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Survey, Questions, Answer
from .serializers import SurveySerializer,QuestionSerializer,AnswerSerializer
from rest_framework import permissions
from rest_framework import viewsets
import urllib

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

# @csrf_exempt
def generate_thumbnail(request):
    data=request.data
    urllib.request.urlretrieve(data['image_url'],"test.jpg")
    image_file=Image.open("test.jpg")
    reduced_image=image_file.resize((50,50), Image.ANTIALIAS)
    reduced_image.save("reduced_image.jpg")
    with open("reduced_image.jpg",'rb') as f:
        return HttpResponse(f.read(),content_type="image/jpeg")