from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import status
from .models import UserProfile, UserProfileImage
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
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
        
        try:
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
                'fullName':userprofile.fullName,
                'username':user.username,
                'phoneNumber':userprofile.phoneNumber,
                'email':user.email,
                'password':'Encrypted'
            }

            return Response(
                data , status= status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response({'message':'Something must have gone wrong. {}'.format(e)}, status.HTTP_400_BAD_REQUEST)

        # create user

        



class GetTokenApi(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user  = authenticate(username = username, password = password)
        if user:
            return Response({'token':user.auth_token.key})
        else:
            return Response({'message':'Wrong Information'}, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request, username):
        try:
            userprofile = UserProfile.objects.get(user__username= username)
            if userprofile:
                data = {
                    'fullName': userprofile.fullName,
                    'username':userprofile.user.username,
                    'email:': userprofile.user.email,
                    'phoneNumber': userprofile.phoneNumber
                }

                return Response(data)
            else:
                return Response({'message':'No user found'}, status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'No user found'}, status = status.HTTP_404_NOT_FOUND)
            print(e)






class UpdateProfilePhotoView(APIView):
    parser_classes = (MultiPartParser, FormParser,)
    permission_classes = (IsAuthenticated,)
    def put(self, request):
        print('Update Profile Picture view called')
        #print(request.data)
        username = request.data.get('username')
        password = request.data.get('password')
        print(username)
        user = User(username = username)
        user.set_password(password)
        user.save()
        userImage=  UserProfileImage(user = user)
        userImage.user.username = username
        userImage.profile_img = request.data.get('image')
        userImage.save()
        return Response({'message':'Profile Photo Updated'})