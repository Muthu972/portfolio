from django.contrib import admin
from django.urls import path,include
from detail.urls import *

urlpatterns = [
    path('super/',include('detail.urls')),


]
# mysite/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('detail.urls')),  # ← connects root URL to your app
]
