
from dataclasses import fields
from django import forms  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  
from django.forms.forms import Form  
from .models import Patient

class Patientform (forms.ModelForm):
    class Meta:
        model=Patient
        fields=['diatype','weight', 'height','age']