from django.urls import path
from . import views
from .views import myrecords
urlpatterns = [
    path('myrecords', views.myrecords, name ='myrecords' ),
    path('editrecord', views.editrecord, name ='editrecord' ),


    ] 