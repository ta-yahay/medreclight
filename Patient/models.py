from datetime import datetime
from django.db import models
from enum import unique
from pyexpat import model
from tabnanny import verbose
from django.db import models
from numpy import choose
from zmq import NULL
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import profile




class Patient (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
    type1='type1'
    type2='type2'
   
    diatype_choices=[
        
        (type1,'type1'),
        (type2,'type2')
    ]
    height= models.IntegerField(null=True)
    weight=models.IntegerField(null=True)
    age=models.IntegerField(null=True)
    diatype=models.CharField (choices=diatype_choices,blank=True,null=True ,max_length=20)
    def __str__ (self):
        return str(self.user)
@receiver(post_save, sender=User)
def create_user_patient(sender, instance, created, **kwargs):
    if created:
        Patient.objects.create(user=instance)

    
    
#     # when a new user sign up ---> blank profile created
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Patient.objects.create(user=instance)

    
    
    
    



    
    
    
    
    
    
# class Rava (models.Patient_info):
#     dya = models.IntegerField()
    
# Create your models here.
