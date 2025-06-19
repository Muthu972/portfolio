from django.contrib import admin
from django.urls import path
from .views import*
from django.urls import path
from . import views 


urlpatterns = [
   
    path('homes/',home),
    path('about/',abouts),
    path('project/',projects),
    path('addmembers/',addmember),
    


]
