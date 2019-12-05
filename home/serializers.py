
from rest_framework import serializers
from .models import UserProfile

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('fullName', 'username', 'email', 'password')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        user = UserProfile(
            fullName = validated_data['fullName'],
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password']
        )
        user.save()
        return user