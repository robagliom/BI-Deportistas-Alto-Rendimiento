from django.contrib import admin
from .models import Lesion

@admin.register(Lesion)
class LesionAdmin(admin.ModelAdmin):
    pass