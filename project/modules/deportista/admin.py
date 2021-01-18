from django.contrib import admin
from django.db import IntegrityError
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DateWidget
from .models import Deportista
from modules.institucion.models import  Institucion

@admin.register(Deportista)
class DeportistaAdmin(admin.ModelAdmin):
    pass

class DeportistaResource(resources.ModelResource):
    institucion = fields.Field(column_name='institucion',attribute='institucion',widget=ForeignKeyWidget(Institucion, 'id'))

    class Meta:
        model = Deportista
        exclude = ('activo',)

    def save_instance(self, instance, using_transactions=True, dry_run=False):
        try:
            super(DeportistaResource, self).save_instance(instance, using_transactions, dry_run)
        except IntegrityError:
            pass        