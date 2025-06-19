from .models import*
from django import forms

class memberdetail(forms.ModelForm):
    class Meta:
        model=details
        fields='__all__'
         