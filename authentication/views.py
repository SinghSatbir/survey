from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from survey_project import settings
from .serializers import UserSerializer, LoginSerializer
from rest_framework import status
from django.contrib import auth
import jwt
# Create your views here.

class RegisterView(GenericAPIView):
    serializer_class = UserSerializer
    def post(self,request):
        serialzer=UserSerializer(data=request.data)
        if(serialzer.is_valid()):
            serialzer.save()
            return Response(serialzer.data,status=status.HTTP_201_CREATED)
        return Response(serialzer.errors,status=status.HTTP_400_BAD_REQUEST)

class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth_token = jwt.encode({'username': user.username}, settings.JWT_SECRET_KEY)
            serializer = UserSerializer(user)
            data = {
                "user": serializer.data,
                "token": auth_token,
            }
            return Response(data, status=status.HTTP_200_OK)

            # SEND RES

        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)