from django.contrib import admin
from .models import DatoObjetivo

@admin.register(DatoObjetivo)
class DatoObjetivoAdmin(admin.ModelAdmin):
    pass