from django.forms import ModelForm
from .models import Deportista

class DeportistaForm(ModelForm):
    class Meta:
        model = Deportista
        exclude = ['activo']