from fnmatch import fnmatch
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# from matplotlib.font_manager import _Weight
# from .models import Plogin
from Patient.models import Patient
from accounts.models import Profile
# from  Patient.forms import Patient_infoForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm




def home(request):
    return render (request,'Pages/phome.html',{})

def login(request):
    return render (request,'registration/login.html',{})

def signup(request):
    return render (request,'registration/signup.html',{})
