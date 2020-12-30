from django.forms import ModelForm
from .models import Institucion

class InstitucionForm(ModelForm):
    class Meta:
        model = Institucion
        exclude = ['activo']