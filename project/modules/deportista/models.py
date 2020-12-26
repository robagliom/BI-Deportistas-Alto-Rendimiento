from django.db import models
from ..institucion.models import Institucion

class Deportista(models.Model):
    documento = models.CharField(max_length=8, unique=True, blank=False)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)
    institucion = models.ForeignKey(Institucion, models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Deportistas"

    def __str__(self):
        return ('{} - {} {}').format(self.documento,self.apellido,self.nombre)