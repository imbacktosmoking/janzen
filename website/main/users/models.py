from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import AbstractUser 


# Create your models here.


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    GENDER_CHOICES = [
        ('Male','Male'),
        ('Female','Female'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age = models.PositiveBigIntegerField()
    email = models.EmailField(max_length=254 )


    def __str__(self):
        return self.user.username