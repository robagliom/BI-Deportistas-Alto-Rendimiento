from django.contrib import admin
from .models import DatoSubjetivo

@admin.register(DatoSubjetivo)
class DatoSubjetivoAdmin(admin.ModelAdmin):
    pass