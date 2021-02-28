# urls.py
from django.urls import path
from . import  views

urlpatterns = [
    path('crear/', views.crear, name='crear_deportista'),
    path('crear_multiple/', views.crear_multiple, name='crear_deportistas'),
    path('editar/', views.editar, name='editar_deportista'),
    path('editar/(?<str:accionOk>;<str:accionReturn>)', views.editar, name='deportista_editado'),
    path('editar_deportista/<int:pk>/', views.DeportistaUpdate.as_view(), name='editar_deportista_pk'),
    path('eliminar/', views.eliminar, name='eliminar_deportista'),
    path('analisiscompleto/', views.analisiscompleto, name='analisiscompleto'),
]