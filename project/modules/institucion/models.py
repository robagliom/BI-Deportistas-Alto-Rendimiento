from django.db import models
from django.urls import reverse

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

    objects = models.Manager()
    class Meta:
        verbose_name_plural = "Instituciones"

    def __str__(self):
        return ('{}').format(self.nombre)

    def get_absolute_url(self):
        return reverse('editar_institucion')