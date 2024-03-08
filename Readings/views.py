from django.shortcuts import render
import pandas
from django.views.generic import ListView
from django.contrib.auth import authenticate
from Readings.forms import BP_form,Glucose_form
from .models import BloodP , Glucose
from accounts.models import Profile

# Create your views here.

# def myrecords(request):
#     bloodp= BloodP.objects.filter(user=request.user)
#     bmi= Bmi.objects.filter(user=request.user)
#     glucose= Glucose.objects.filter(user=request.user)

#     return render(request , 'readings/myrecords.html' ,{
#         'bloodp': bloodp,
#         'bmi': bmi ,
#         'gluecose':glucose})
def editrecord(request):
    # profile=Profile.objects.get(user=request.user)
    if request.method=="POST":
        # profile=Profile.objects.get(user=request.user)
        blood=BP_form(request.POST,instance=request.user)
        glucose=Glucose_form(request.POST,instance=request.user)  
        if blood.is_valid:
            blood.save()
            blood.user =request.user
            blood.save()
        if glucose.is_valid:
            glucose.save()
            glucose.user= request.user
            glucose.save()
        BP_set=BloodP.objects.filter(user=request.user)
        glu_set=Glucose.objects.filter(user=request.user)
        BP_ordered=BP_set.order_by('date')[:500]
        glu_ordered=glu_set.order_by('date')[:500]
        profile=Profile.objects.get(user=request.user)
        return render(request , 'accounts/profile.html',{
            'profile':profile,
            'BP':BP_ordered,
            'glucose':glu_ordered})
    
    else:
        blood=BP_form()
        glucose=Glucose_form()    
    return render (request , 'readings/editrecord.html',{
        'blood': blood,
        'gluecose':glucose})
