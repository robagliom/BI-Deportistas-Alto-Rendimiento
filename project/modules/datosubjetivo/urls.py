# urls.py
from django.urls import path
from . import  views

urlpatterns = [
    path('datossubjetivos/', views.datossubjetivos, name='datossubjetivos'),
]