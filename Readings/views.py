from django.shortcuts import render
import pandas
from django.views.generic import ListView
from django.contrib.auth import authenticate
from Readings.forms import BP_form, Bmi_form,BloodP,Glucose_form
from .models import BloodP ,Bmi, Glucose
from accounts.models import Profile

# Create your views here.

def myrecords(request):
    bloodp= BloodP.objects.filter(user=request.user)
    bmi= Bmi.objects.filter(user=request.user)
    glucose= Glucose.objects.filter(user=request.user)

    return render(request , 'readings/myrecords.html' ,{
        'bloodp': bloodp,
        'bmi': bmi ,
        'gluecose':glucose})
def editrecord(request):
    if request.method=="POST":
        bmi=Bmi_form(request.POST,instance=request.user)
        blood=BP_form(request.POST,instance=request.user)
        glucose=Glucose_form(request.POST,instance=request.user)  
        if bmi.is_valid:
            bmi.save(commit=False)
            bmi.user = request.user
            bmi.save()
        if blood.is_valid:
            blood.save(commit=False)
            blood.user =request.user
            blood.save()
        if glucose.is_valid:
            glucose.save(commit=False)
            glucose.user= request.user
            glucose.save()
        return render(request , 'readings/myrecords.html',{'blood': blood,
        'bmi': bmi ,
        'gluecose':glucose})

    else:
        bmi=Bmi_form()
        blood=BP_form()
        glucose=Glucose_form()    


    return render (request , 'readings/editrecord.html',{
        'blood': blood,
        'bmi': bmi ,
        'gluecose':glucose})
