from django.contrib import admin
from .models import Enfermedad

@admin.register(Enfermedad)
class EnfermedadAdmin(admin.ModelAdmin):
    pass