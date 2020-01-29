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
    createdOn = models.DateTimeField(auto_now_add=True)
    #profile_img = models.ImageField(upload_to = 'profile_images/', null = True)

    
    def __str__(self):
        return self.user.username

    

class RentPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length = 20)
    description = models.CharField(max_length = 150)
    area = models.CharField(max_length = 40)
    rent = models.IntegerField()
    numBedroom = models.IntegerField()
    numBathroom = models.IntegerField()
    numFloor = models.IntegerField()
    imageReference = models.CharField(max_length = 150)
    
    def __str__(self):
        return f'{self.user.username}:{self.imageReference}'
    