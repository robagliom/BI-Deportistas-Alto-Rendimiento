from django.contrib import admin
from django.db import IntegrityError
from django.utils.translation import gettext as _
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DateWidget
from .models import DatoSubjetivo
from modules.deportista.models import Deportista

@admin.register(DatoSubjetivo)
class DatoSubjetivoAdmin(admin.ModelAdmin):
    pass

class DatoSubjetivoResource(resources.ModelResource):
    deportista = fields.Field(column_name='deportista',attribute='deportista',widget=ForeignKeyWidget(Deportista, 'documento'))
    fecha = fields.Field(column_name='fecha',attribute='fecha',widget=DateWidget())
    colorIn = fields.Field(attribute='get_colorIn_display', column_name=_(u'colorIn'))
    colorOut = fields.Field(attribute='get_colorOut_display', column_name=_(u'colorOut'))

    class Meta:
        model = DatoSubjetivo

    def save_instance(self, instance, using_transactions=True, dry_run=False):
        try:
            super(DatoSubjetivoResource, self).save_instance(instance, using_transactions, dry_run)
        except IntegrityError:
            pass        