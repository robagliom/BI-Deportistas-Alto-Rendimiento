# urls.py
from django.urls import path
from . import  views

urlpatterns = [
    path('crear/', views.crear, name='crear_institucion'),
    path('editar/', views.editar, name='editar_institucion'),
    path('editar/(?<str:accionOk>;<str:accionReturn>)', views.editar, name='institucion_editado'),
    path('editar_institucion/<int:pk>/', views.InstitucionUpdate.as_view(), name='editar_institucion_pk'),
    path('eliminar/', views.eliminar, name='eliminar_institucion'),
]