from django.db import models

class Permiso(models.Model):
    codigo = models.CharField(max_length=3, unique=True)
    nombre = models.CharField(max_length=50,null=True)
    descripcion = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "Permisos"

    def __str__(self):
        return ('{} - {}').format(self.codigo,self.nombre)