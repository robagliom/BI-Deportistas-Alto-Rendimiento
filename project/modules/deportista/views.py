from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from tablib import Dataset 
from modules.auxiliar.views import usuario_logueado
from modules.institucion.models import Institucion
from .models import Deportista
from .forms import DeportistaForm
from .admin import  DeportistaResource

@login_required
def crear(request):
    accionOk = None
    accionReturn = None
    if request.method == 'POST':
        form = DeportistaForm(request.POST)
        if form.is_valid():
            try:
                accionOk = True
                deportista = form.save()
                accionReturn = 'El deportista {} ha sido creado correctamente.'.format(deportista)
            except Exception as e:
                accionOk = False
                accionReturn = "Ocurrió un error al crear deportista. Error: {}".format(e)
    form = DeportistaForm()
    form.fields['institucion'].queryset = Institucion.objects.filter(activo=True)

    c = {
        'usuario_logueado':True,
        'usuario':request.user.username,
        'nav_id':'nav_deportistas',
        'form': form,
        'accionOk': accionOk,
        'accionReturn': accionReturn,
        }
    return render(request, 'deportista/deportista_crear.html',context=c)

@login_required
def crear_multiple(request):
    accionOk = None
    accionReturn = None
    instituciones = Institucion.objects.filter(activo=True)

    if request.method == 'POST':
        try:
            institucion = request.POST['institucion_select']
            datos_resource = DeportistaResource()        
            dataset = Dataset()
            nuevos_datos = request.FILES['deportistasxlsfile']
            dataset.load(nuevos_datos.read())
            institucion_col = [institucion for i in range(dataset.height)]
            dataset.append_col(institucion_col,header="institucion")
            datos_resource.import_data(dataset, dry_run=False)
            accionOk = True
            accionReturn = "Los deportistas han sido creado correctamente."
        except Exception as e:
            accionOk = False
            accionReturn = "Ocurrió un error al crear los deportistas. Error: {}".format(e)

    c = {
        'usuario_logueado':True,
        'usuario':request.user.username,
        'nav_id':'nav_deportistas',
        'accionOk': accionOk,
        'accionReturn': accionReturn,
        'instituciones': instituciones,
        }
    return render(request, 'deportista/deportista_crear_multiple.html',context=c)


class DeportistaUpdate(UpdateView):
    model = Deportista
    fields = ['documento','nombre','apellido','institucion']
    template_name = 'deportista/deportista_editar.html'
    success_url = reverse_lazy('deportista_editado',kwargs={'accionOk':True,'accionReturn':'Deportista editado correctamente.'})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['deportista_select'] = True
        context['usuario_logueado']=True
        context['usuario']=self.request.user.username
        context['deportistas']=Deportista.objects.filter(activo=True)
        context['nav_id']='nav_deportistas'
        context['form'].fields['institucion'].queryset = Institucion.objects.filter(activo=True)
        return context

    def form_invalid(self, form):
        return reverse_lazy('deportista_editado',kwargs={'accionOk':False,'accionReturn':'Error: {}.'.format(form.errors)})

@login_required
def editar(request,accionOk=None,accionReturn=None):
    deportistas = Deportista.objects.filter(activo=True)
    
    c = {
        'usuario_logueado':True,
        'usuario':request.user.username,
        'nav_id':'nav_deportistas',
        'deportistas':deportistas,
        'accionOk':accionOk,
        'accionReturn':accionReturn,
        }
    return render(request, 'deportista/deportista_editar.html',context=c)

@login_required
def eliminar(request):
    accionOk = None
    accionReturn = None
    deportistas = Deportista.objects.filter(activo=True)

    if request.method == 'POST':
        try:
            deportista_eliminado = Deportista.objects.get(pk=int(request.POST['deportista_pk']))
            deportista_eliminado.activo = False
            deportista_eliminado.save()
            accionOk = True
            accionReturn = 'El deportista {} ha sido eliminada correctamente.'.format(deportista_eliminado)
        except Exception as e:
            accionOk = False
            accionReturn = "Ocurrió un error al eliminar el deportista. Error: {}".format(e) 
    c = {
        'usuario_logueado':True,
        'usuario':request.user.username,
        'nav_id':'nav_deportistas',
        'deportistas':deportistas,
        'accionOk':accionOk,
        'accionReturn':accionReturn,
        }
    return render(request, 'deportista/deportista_eliminar.html',context=c)

@login_required
def analisiscompleto(request):
    c = usuario_logueado(request)
    return render(request, 'visualizaciones/análisisCompleto.html',context=c)