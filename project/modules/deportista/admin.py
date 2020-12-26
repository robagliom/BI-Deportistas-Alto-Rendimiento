from django.contrib import admin
from .models import Deportista

@admin.register(Deportista)
class DeportistaAdmin(admin.ModelAdmin):
    pass