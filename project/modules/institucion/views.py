from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from modules.auxiliar.views import usuario_logueado
from .models import Institucion
from .forms import InstitucionForm

@login_required
def crear(request):
    accionOk = None
    accionReturn = None
    if request.method == 'POST':
        form = InstitucionForm(request.POST)
        if form.is_valid():
            try:
                accionOk = True
                institucion = form.save()
                accionReturn = 'La institución {} ha sido creado correctamente.'.format(institucion)
            except Exception as e:
                accionOk = False
                accionReturn = "Ocurrió un error al crear institución. Error: {}".format(e)
    form = InstitucionForm()

    c = {
        'usuario_logueado':True,
        'usuario':request.user.username,
        'nav_id':'nav_instituciones',
        'form': form,
        'accionOk': accionOk,
        'accionReturn': accionReturn,
        }
    return render(request, 'institucion/institucion_crear.html',context=c)

class InstitucionUpdate(UpdateView):
    model = Institucion
    fields = ['nombre','codPostal','direccion','ciudad','provincia','pais','email','telefono']
    template_name = 'institucion/institucion_editar.html'
    success_url = reverse_lazy('institucion_editado',kwargs={'accionOk':True,'accionReturn':'Institución editada correctamente.'})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['institucion_select'] = True
        context['usuario_logueado']=True
        context['usuario']=self.request.user.username
        context['instituciones']=Institucion.objects.filter(activo=True)
        context['nav_id']='nav_instituciones'
        return context

    def form_invalid(self, form):
        return reverse_lazy('institucion_editado',kwargs={'accionOk':False,'accionReturn':'Error: {}.'.format(form.errors)})

@login_required
def editar(request,accionOk=None,accionReturn=None):
    instituciones = Institucion.objects.filter(activo=True)
    
    c = {
        'usuario_logueado':True,
        'usuario':request.user.username,
        'nav_id':'nav_instituciones',
        'instituciones':instituciones,
        'accionOk':accionOk,
        'accionReturn':accionReturn,
        }
    return render(request, 'institucion/institucion_editar.html',context=c)

@login_required
def eliminar(request):
    accionOk = None
    accionReturn = None
    instituciones = Institucion.objects.filter(activo=True)

    if request.method == 'POST':
        try:
            institucion_eliminado = Institucion.objects.get(pk=int(request.POST['institucion_pk']))
            institucion_eliminado.activo = False
            institucion_eliminado.save()
            accionOk = True
            accionReturn = 'La institución {} ha sido eliminada correctamente.'.format(institucion_eliminado)
        except Exception as e:
            accionOk = False
            accionReturn = "Ocurrió un error al eliminar la institución. Error: {}".format(e) 
    c = {
        'usuario_logueado':True,
        'usuario':request.user.username,
        'nav_id':'nav_instituciones',
        'instituciones':instituciones,
        'accionOk':accionOk,
        'accionReturn':accionReturn,
        }
    return render(request, 'institucion/institucion_eliminar.html',context=c)