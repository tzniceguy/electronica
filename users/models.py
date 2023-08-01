from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    firstname = models.CharField(max_length=30, blank=True)
    lastname = models.CharField(max_length=30, blank=True)
    address= models.CharField(max_length=30, blank=True)
    phonenumber= models.IntegerField(blank=True)
    dob=models.DateField(blank=True)
    
    def __str__(self):
        return self.username
