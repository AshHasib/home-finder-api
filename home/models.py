from django.db import models

# Create your models here.

class UserProfile(models.Model):
    fullName = models.CharField(max_length = 80)
    username = models.CharField(max_length = 50)
    email = models.EmailField()
    password = models.CharField(max_length = 30)

    def __str__(self):
        return self.username