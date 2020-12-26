from django.db import models
from ..deportista.models import Deportista

class DatoObjetivo(models.Model):
    evento = models.CharField(max_length=50)
    fecha = models.DateTimeField(null=True)
    distanceTotal = models.DecimalField(null=True, max_digits=8,decimal_places=2)
    mphi = models.DecimalField(null=True, max_digits=8,decimal_places=2)
    d_mp5 = models.DecimalField(null=True, max_digits=8,decimal_places=2)
    d_mphi = models.DecimalField(null=True, max_digits=8,decimal_places=2)
    velMayor16 = models.DecimalField(null=True, max_digits=8,decimal_places=2)
    velEntre16y20 = models.DecimalField(null=True, max_digits=8,decimal_places=2)
    velEntre20y25 = models.DecimalField(null=True, max_digits=8,decimal_places=2)
    acceleration = models.DecimalField(null=True, max_digits=8,decimal_places=2)
    deceleration = models.DecimalField(null=True, max_digits=8,decimal_places=2)
    mpmi = models.DecimalField(null=True, max_digits=8,decimal_places=2)
    velMax = models.DecimalField(null=True, max_digits=8,decimal_places=2)
    totalTime = models.DecimalField(null=True, max_digits=8,decimal_places=2)
    eee = models.DecimalField(null=True, max_digits=8,decimal_places=2)
    deportista = models.ForeignKey(Deportista, models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Datos Objetivos"
        
    def __str__(self):
        return ('{} - {} - {}').format(self.pk,self.evento,self.deportista)