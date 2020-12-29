# urls.py
from django.urls import path
from . import  views

urlpatterns = [
    path('crear', views.crear, name='crear_usuario'),
    path('editar', views.editar, name='editar_usuario'),
    path('eliminar', views.eliminar, name='eliminar_usuario'),
]