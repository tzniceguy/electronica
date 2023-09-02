from django.contrib.auth.models import AbstractUser, UserManager as AbstractUserManager
from django.db import models
from django.utils import timezone
from PIL import Image
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=0)
    discount = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name

class CustomUserManager(AbstractUserManager):
    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, username, password, **extra_fields)

class CustomUser(AbstractUser):
    '''Fields that are used in authentication of customer/user'''
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=15, unique=True)
    phonenumber= models.IntegerField(blank=True, null=True)

    '''Additional fields that are not used in authentications but
    contains data about the user/customer'''
    firstname = models.CharField(max_length=30, blank=True)
    lastname = models.CharField(max_length=30, blank=True)
    address= models.CharField(max_length=30, blank=True)
    dob=models.DateField(blank=True,null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

  