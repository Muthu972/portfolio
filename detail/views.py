from django.shortcuts import render,redirect
from detail.urls import*
from .models import*
from .form import*
from django.views import View
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponse






def home(request):
    data={"detail":details.objects.all()}
    return HttpResponse(request,'home.html',data)

    
def abouts(request):
    data={"detail":details.objects.all()}
    return render(request,'about.html',data)



    
def addmember(request):
    data={"members":memberdetail}
    if request.method == "POST":
        member=memberdetail(request.POST)
        if member.is_valid():
            member.save()
    return render(request,'contact.html',data)



   

def projects(request):
    data={"detail":details.objects.all()}
    return render(request,'project.html',data)
   

 
    


    