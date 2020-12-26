from django.db import models
from ..permiso.models import Permiso

class Usuario(models.Model):
    documento = models.CharField(max_length=8, unique=True, blank=False)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)
    permisos = models.ManyToManyField(Permiso)