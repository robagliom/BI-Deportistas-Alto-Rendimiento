from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from modules.auxiliar.views import usuario_logueado

@login_required
def datossubjetivos(request):
    c = usuario_logueado(request)
    return render(request, 'visualizaciones/datosSubjetivos.html',context=c)