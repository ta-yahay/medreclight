from distutils.command.upload import upload
from email.policy import default
from statistics import mode
from django.db import models
from matplotlib.pyplot import cla
# from pages.models import Dlogin
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import profile
from accounts.models import Profile

class Doctor (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ssn=models.CharField (unique=True, max_length=50,blank=True)
    phone=models.CharField (max_length=50,blank=True)
    address=models.CharField(max_length=70,blank= True,null=True)
    city=models.CharField(max_length=70,blank= True,null=True)
    photo= models.ImageField(upload_to='media/doctor', default='media/doctor/download.png')


    def __str__ (self):
        return str(self.user)   
         
#     # when a new user sign up ---> blank profile created
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Doctor.objects.create(user=instance)

    



# Create your models here.
