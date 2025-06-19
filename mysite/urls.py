from django.contrib import admin
from django.urls import path,include
from detail.urls import *

urlpatterns = [
    path('super/',include('detail.urls')),


]


