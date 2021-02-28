# urls.py
from django.urls import path
from . import  views

urlpatterns = [
    path('datosobjetivos/', views.datosobjetivos, name='datosobjetivos'),
]