from django.db import models

class Institucion(models.Model):
    nombre = models.CharField(max_length=50)
    codPostal = models.CharField(max_length=4)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Instituciones"

    def __str__(self):
        return ('{} - {}').format(self.pk,self.nombre)