from django.contrib import admin
from django.db import IntegrityError
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DateWidget
from .models import Enfermedad
from modules.deportista.models import Deportista

@admin.register(Enfermedad)
class EnfermedadAdmin(admin.ModelAdmin):
    pass

class EnfermedadResource(resources.ModelResource):
    deportista = fields.Field(column_name='deportista',attribute='deportista',widget=ForeignKeyWidget(Deportista, 'documento'))
    fecha = fields.Field(column_name='fecha',attribute='fecha',widget=DateWidget())

    class Meta:
        model = Enfermedad

    def save_instance(self, instance, using_transactions=True, dry_run=False):
        try:
            super(EnfermedadResource, self).save_instance(instance, using_transactions, dry_run)
        except IntegrityError:
            pass        