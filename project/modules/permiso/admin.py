from django.contrib import admin
from .models import Permiso

@admin.register(Permiso)
class PermisoAdmin(admin.ModelAdmin):
    pass