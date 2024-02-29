from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import Profile
from .models import Patient
from accounts.models import Profile
# from .forms import Patient_infoForm
def patient (request ,ssn):
    profile= Profile.objects.get(ssn=ssn)
    return render(request,'patient/patient.html')

def pedit_record(request ,ssn):
    profile= Profile.objects.get(ssn=ssn)
    return render(request,'patient/pedit_record.html')


def update_data (request,ssn):
    profile= Profile.objects.get(ssn=ssn)
    return render(request,'patient/update_data.html')



def pprediction(request,ssn):
    profile= Profile.objects.get(ssn=ssn)
    return render(request,'patient/pprediction.html', {'profile': profile})    


def pprofile(request,ssn):
    profile= Profile.objects.get(ssn=ssn)
    
    
    
    
    # id= Patient_info.objects.all(ssn='12345678')
    ssn=Profile.ssn
    phone=Profile.phone
    city=Profile.city
    gender=Profile.gender
    address=Profile.address

    hieght = Patient.height
    wieght= Patient.weight
    dtype=Patient.diatype


    # photo=Doctor_info.d_photo
    return render(request,'patient/pprofile.html',{
        
        "ssn":ssn,
        "wieght":wieght,
        "hieght": hieght,
        "dtype": dtype,
        "gender": gender,
        "phone":phone,
        "city":city,
        "address":address
        
    })

    


def precord(request,ssn):
    return render(request,'patient/precord.html')



# def register(request):
#     fname= request.POST.get('first_name')
#     lname= request.POST.get('last_name')
#     ssn= request.POST.get('SSN')
#     password= request.POST.get('password')
#     email= request.POST.get('email')
#     phone= request.POST.get('phone')
#     city= request.POST.get('city')
#     address= request.POST.get('address')
#     height= request.POST.get('height')
#     weight= request.POST.get('weigh')
#     age= request.POST.get('Age')
#     diatype= request.POST.get('Diabetestype')
#     gender= request.POST.get('gender')
   
   
#     data = patient_info (fname=fname,lname=lname,ssn=ssn,
#     password=password,email=email,phone=phone,city=city,
#     address=address,height=height,weight=weight,age=age,
#     diatype=diatype,gender=gender)
#     data.save()

#     return render(request,'register.html')

# # Create your views here.



# # Create your views here.
