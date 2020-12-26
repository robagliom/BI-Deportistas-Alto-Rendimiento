from django.db import models
from ..permiso.models import Permiso
from ..institucion.models import Institucion

class Usuario(models.Model):
    documento = models.CharField(max_length=8, unique=True, null=False)
    nombre = models.CharField(max_length=50,null=True)
    apellido = models.CharField(max_length=50,null=True)
    email = models.EmailField(null=False)
    telefono = models.CharField(max_length=20,null=True)
    contraseña = models.CharField(max_length=50,null=False)
    activo = models.BooleanField(default=True)
    permisos = models.ManyToManyField(Permiso)
    institucion = models.ForeignKey(Institucion, models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return ('{} - {} {}').format(self.documento,self.apellido,self.nombre)