from django.db import models

class Permiso(models.Model):
    codigo = models.CharField(max_length=3, unique=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()