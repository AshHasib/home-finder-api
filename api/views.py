from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import status
from .models import UserProfile
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
# Create your views here.


class HelloApi(APIView):
    
    def get(self, request):
        return Response({'message':'Hello this is your API being called'})


class AuthHelloApi(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response({'message':'Hello this is your API being called using token'})


class Register(APIView):

    def post(self, request):
        fullName = request.data.get('fullName')
        username = request.data.get('username')
        phoneNumber = request.data.get('phoneNumber')
        password = request.data.get('password')
        email = request.data.get('email')


        # create user

        user = User(
            username = username,
            email = email,
        )
        user.set_password(password)

        user.save()

        userprofile = UserProfile(
            user = user,
            fullName = fullName,
            phoneNumber = phoneNumber,
        )
        userprofile.save()
        Token.objects.create(user = user)
        data = {
            'username':user.username,
            'email':user.email
        }

        return Response(
            data , status= status.HTTP_201_CREATED
        )



class GetTokenApi(APIView):

    def post(self, request):

        username = request.data.get('username')
        password = request.data.get('password')

        user  = authenticate(username = username, password = password)

        if user:
            return Response({'token':user.auth_token.key})
        else:
            return Response({'message':'Wrong Information'})


