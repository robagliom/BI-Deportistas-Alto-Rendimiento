# urls.py
from django.urls import path
from . import  views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout', views.logout_view, name='logout'),
    path('login_template', views.login_template, name='login_template'),
    path('login', views.login_view, name='login'),
    path('importar/', views.importar, name='importar'),
]