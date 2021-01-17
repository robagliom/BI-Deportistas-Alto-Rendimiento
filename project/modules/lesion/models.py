from django.db import models
from ..deportista.models import Deportista

class Lesion(models.Model):
    deportista = models.ForeignKey(Deportista, models.SET_NULL, null=True)
    fecha = models.DateTimeField(null=True)
    diagnosticoInicial = models.CharField(max_length=200, null=True)
    diagnosticoFinal = models.CharField(max_length=200, null=True)
    gravedad = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name_plural = "Lesiones"

    def __str__(self):
        return ('{} - {} - {}').format(self.pk,self.fecha,self.deportista)