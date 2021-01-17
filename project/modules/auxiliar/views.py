from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import datetime
from tablib import Dataset 
from . import views
from modules.usuario.models import Usuario
from modules.datoobjetivo.admin import DatoObjetivoResource
from modules.datosubjetivo.admin import DatoSubjetivoResource
from modules.lesion.admin import LesionResource
from modules.enfermedad.admin import EnfermedadResource

def index(request):
    c = usuario_logueado(request)
    return render(request, 'index.html',context=c)

def usuario_logueado(request):
    usuario_logueado = False
    usuario = None

    if request.user.is_authenticated:
        usuario_logueado = True
        try:
            usuario = Usuario.objects.get(documento=request.user.username).nombre
        except:
            usuario = request.user.username

    c = {
            'usuario_logueado':usuario_logueado,
            'usuario':usuario,
         }
    return c

def logout_view(request):
    logout(request)
    return redirect(reverse(views.index))

def login_template(request,error=False):
    return render(request,'login.html',context={'error':error})

def login_view(request):
    username = request.POST['documento']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(reverse(views.index))    
    else:
        return login_template(request,True)

@login_required
def importar(request):
    c = usuario_logueado(request)
    accionOk = None
    accionReturn = None
    if request.method == 'POST':  
        try:
            tipo_import = request.POST['tipo_dato_select']
            if tipo_import == 'DatoObjetivo':
                datos_resource = DatoObjetivoResource()
            elif tipo_import == 'DatoSubjetivo':
                datos_resource = DatoSubjetivoResource()
            elif tipo_import == 'Lesion':
                datos_resource = LesionResource()
            elif tipo_import == 'Enfermedad':
                datos_resource = EnfermedadResource()        
            dataset = Dataset()
            nuevos_datos = request.FILES['xlsfile']  
            dataset.load(nuevos_datos.read())
            datos_resource.import_data(dataset, dry_run=False)
            accionOk = True
            accionReturn = 'Los datos se importaron correctamente.'
        except Exception as e:
            accionOk = False
            accionReturn = 'Algo salió mal. Error: {}'.format(e)
    c['accionOk'] = accionOk
    c['accionReturn'] = accionReturn
    return render(request, 'importar/importar.html',context=c)

@login_required
def exportar(request):
    c = usuario_logueado(request)
    return render(request, 'exportar/exportar.html',context=c)

@login_required
def exportar_datos(request):
    c = usuario_logueado(request)
    if request.method == 'POST':  
        try:
            tipo_export = request.POST['tipo_dato_select']
            if tipo_export == 'DatoObjetivo':
                datos_resource = DatoObjetivoResource()
                nombre_export = "DatosObjetivos"
            elif tipo_export == 'DatoSubjetivo':
                datos_resource = DatoSubjetivoResource()
                nombre_export = "DatosSubjetivos"
            elif tipo_export == 'Lesion':
                datos_resource = LesionResource()
                nombre_export = "Lesiones"
            elif tipo_export == 'Enfermedad':
                datos_resource = EnfermedadResource()
                nombre_export = "Enfermedades"
            # else:
            #     datos_resource = TodosResource()
            dataset = datos_resource.export()
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="{}_{}.xls"'.format(datetime.datetime.now().strftime('%Y-%m-%d-%H%M'),nombre_export)
            return response
        except Exception as e:
            accionOk = False
            accionReturn = 'Algo salió mal. Error: {}'.format(e)
            c['accionOk'] = accionOk
            c['accionReturn'] = accionReturn
            return render(request, 'exportar/exportar.html',context=c)    