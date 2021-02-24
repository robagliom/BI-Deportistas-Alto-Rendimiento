from django.shortcuts import render
from modules.auxiliar.views import usuario_logueado

def lesionesenfermedades(request):
    c = usuario_logueado(request)
    return render(request, 'visualizaciones/lesionesenfermedades.html',context=c)