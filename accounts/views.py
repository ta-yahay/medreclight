from audioop import reverse
from telnetlib import BM
from unicodedata import decimal
from unittest import result
from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import Signupform, Userform ,Profileform
from django import forms
from .models import Profile
from Patient.models import Patient
import pandas
from django.views.generic import ListView
from Readings.utils import get_chart
from Readings.models import BloodP, Bmi
from Readings.models import Glucose
from Readings.models import BloodP
from Readings.urls import urlpatterns
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = Signupform(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = Signupform()
    return render(request, 'registration/signup.html', {'form': form})

def profile(request):
    BP_set=BloodP.objects.filter(user=request.user)
    BMI_set=Bmi.objects.filter(user=request.user)
    glu_set=Glucose.objects.filter(user=request.user)
    BP_ordered=BP_set.order_by('date')[:500]
    BMI_ordered=BMI_set.order_by('date')[:500]
    glu_ordered=glu_set.order_by('date')[:500]
    profile=Profile.objects.get(user=request.user)
    return render(request , 'accounts/profile.html',{
        'profile':profile,
        'BP':BP_ordered,
        'BMI':BMI_ordered,
        'glucose':glu_ordered})



def edit_profile(request):
    profile=Profile.objects.get(user=request.user)
    if request.method=="POST":
        userform=Userform(request.POST,instance=request.user)
        profileform=Profileform(request.POST, instance=profile)  
        if userform.is_valid and profileform.is_valid:
            userform.save()
            change=profileform.save(commit=False)
            change.user=request.user
            change.save()
            return render(request , 'accounts/profile.html',{'profile':profile})

    else:
        userform=Userform(instance=request.user)
        profileform=Profileform(instance=profile)    


    return render (request , 'accounts/edit_profile.html',{'userform':userform, 'profileform':profileform})

def patient_profile(request):
    if request.method == "GET":
        dsearch=request.GET['dsearch'] 
        profile=Profile.objects.filter(ssn =dsearch)
        
        return render (request,'accounts/patient_profile.html',{'profile':profile})
    else:
      return render (request,'accounts/profile.html',{})
        
    











# def Patient_profile(request):
#     if request.method == "POST":
#         dsearch=request.POST['dsearch'] 
#         Profiles= Profile.objects.get(ssn = dsearch)
#         return render (request,'accounts/patient_profile.html',{'dsearch':dsearch, 'Profile':Profile})
#     else:
#       return render (request,'accounts/profile',{})

    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data ['username']
    #         password = form.cleaned_data['password1']
    #         user=authenticate(username = username , password = password)
    #         login (request,user)
    #         return redirect ('pprofile')
        