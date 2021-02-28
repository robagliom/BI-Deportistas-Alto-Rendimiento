from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from modules.auxiliar.views import usuario_logueado

@login_required
def datosobjetivos(request):
    c = usuario_logueado(request)
    return render(request, 'visualizaciones/datosObjetivos.html',context=c)