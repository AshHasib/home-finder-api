from django.shortcuts import render
from django.http import JsonResponse
from .serializers import UserSerializer
from rest_framework import generics

# Create your views here.

def index(request):
    
    data = {
        'message':'Hello, This is an API'
    }

    return JsonResponse(data, safe= False)


class CreateUser(generics.CreateAPIView):
    serializer_class = UserSerializer