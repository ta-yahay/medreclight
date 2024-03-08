from django import forms
from django.forms.forms import Form  
from .models import BloodP,Glucose



class BP_form (forms.ModelForm):
    class Meta:
        model=BloodP
        fields=['value','date','image']
        
class Glucose_form (forms.ModelForm):
    class Meta:
        model=Glucose
        fields=['value','date','image']