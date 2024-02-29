from django.urls import path
from . import views

urlpatterns = [
    path('dedit_record', views.dedit_record, name ='dedit_record' ),
    path('dprediction', views.dprediction, name ='dprediction' ),
    path('dprofile', views.dprofile, name ='dprofile' ),
    path('drecord', views.drecord, name ='drecord' ),
    path('dmedication_err', views.dmedication_err, name ='dmedication_err' ),

    ] 