from django.urls import path
from . import views
# from .views import myrecords
urlpatterns = [
    path('editrecord', views.editrecord, name ='editrecord' ),
    ] 