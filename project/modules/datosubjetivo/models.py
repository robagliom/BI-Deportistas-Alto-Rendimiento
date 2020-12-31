from django.db import models
from ..deportista.models import Deportista

class DatoSubjetivo(models.Model):
    COLORES = [
        ('VE', 'Verde'),
        ('RO', 'Rojo'),
        ('AM', 'Amarillo')
    ]
    fecha = models.DateTimeField(null=True)
    inpregunta1	= models.CharField(max_length=50,null=True)
    inpregunta2	= models.CharField(max_length=50,null=True)
    inpregunta2a = models.CharField(max_length=50,null=True)
    inpregunta3	= models.CharField(max_length=50,null=True)
    inpregunta4	= models.CharField(max_length=50,null=True)
    colorIn = models.CharField(max_length=2,choices=COLORES,default='VE')
    outpregunta1 = models.CharField(max_length=50,null=True)
    colorOut = models.CharField(max_length=2,choices=COLORES,default='VE')
    deportista = models.ForeignKey(Deportista, models.SET_NULL,null=True)

    class Meta:
        verbose_name_plural = "Datos Subjetivos"

    def __str__(self):
        return ('{} - {} - In: {} Out: {}').format(self.pk,self.deportista,self.colorIn,self.colorOut)
