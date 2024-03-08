from django.db import models
from django.conf import settings
from datetime import datetime
from enum import unique
from pyexpat import model
from tabnanny import verbose
from numpy import choose
# from pages.models import Plogin
from zmq import NULL
from django.contrib.postgres.fields import ArrayField
from Patient.models import Patient
from django.contrib.auth.models import User
from django.utils.timezone import now




# Create your models here.   
class BloodP(models.Model):
    user =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    value= models.DecimalField( max_digits=5, decimal_places=2, null=False)
    date=models.DateTimeField(default=datetime.now,blank=True)
    def __repr__ (self):
        return "{}-{}-{}".format(self.user,self.value, self.date)



class Glucose(models.Model):
    user =models.ForeignKey(User ,on_delete=models.CASCADE)
    value=models.DecimalField( max_digits=5, decimal_places=2, null=False)
    date=models.DateTimeField(default=datetime.now, blank=True)
    def __str__ (self):
        return "{}-{}-{}".format(self.user,self.value, self.date)
