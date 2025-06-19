from django.db import models
from django.forms import ModelForm

class details(models.Model):
    name=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=100,null=True)
    mobile=models.CharField(max_length=100,null=True)
    whatsapp=models.CharField(max_length=100,null=True)
    location=models.CharField(max_length=100,null=True)
   
    


