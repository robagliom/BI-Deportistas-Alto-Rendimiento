# urls.py
from django.urls import path
from . import  views

urlpatterns = [
    path('crear/', views.crear, name='crear_usuario'),
    path('editar/', views.editar, name='editar_usuario'),
    path('editar/(?<str:accionOk>;<str:accionReturn>)', views.editar, name='usuario_editado'),
    path('editar_usuario/<int:pk>/', views.UsuarioUpdate.as_view(), name='editar_usuario_pk'),
    path('eliminar/', views.eliminar, name='eliminar_usuario'),
]