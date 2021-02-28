from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from modules.auxiliar.views import usuario_logueado

@login_required
def lesionesenfermedades(request):
    c = usuario_logueado(request)
    return render(request, 'visualizaciones/lesionesenfermedades.html',context=c)