from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    fullName = models.CharField(max_length = 50)
    phoneNumber = models.CharField(max_length = 20)
    #profile_img = models.ImageField(upload_to = 'profile_images/', null = True)

    
    def __str__(self):
        return self.user.username


class UserProfileImage(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key = True
    )
    profile_img = models.ImageField(upload_to = 'profile_images/', blank = True, null = True)


    def __str__(self):
        return self.user.username
    