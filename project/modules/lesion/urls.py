# urls.py
from django.urls import path
from . import  views

urlpatterns = [
    path('lesionesenfermedades/', views.lesionesenfermedades, name='lesionesenfermedades'),
]