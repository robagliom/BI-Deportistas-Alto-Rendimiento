from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
import string
import random
from settings.local import EMAIL_HOST_USER
from modules.auxiliar.views import usuario_logueado
from modules.institucion.models import Institucion
from .models import Usuario
from .forms import UsuarioForm

@login_required
def crear(request):
    accionOk = None
    accionReturn = None
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            accionOk = True
            usuario = form.save(commit=False)
            contraseña = password_generator()
            usuario.contraseña = contraseña
            usuario.save()
            user = User.objects.create_user(usuario.documento,usuario.email,usuario.contraseña)
            user.save()
            try:
                send_mail(
                    'Datos de ingreso BI en Deportistas de Alto Rendimiento',
                    'Usuario: {}. Contraseña: {}'.format(usuario.documento, contraseña),
                    EMAIL_HOST_USER,
                    [usuario.email],
                    fail_silently=False,
                )
                accionReturn = 'El usuario {} {} ha sido creado correctamente.'.format(usuario.nombre,usuario.apellido)
            except Exception as e:
                accionOk = False
                accionReturn = "Ocurrió un error al enviar los datos de acceso por email. Error: {}".format(e)
    form = UsuarioForm()
    form.fields['institucion'].queryset = Institucion.objects.filter(activo=True)

    c = {
        'usuario_logueado':True,
        'usuario':request.user.username,
        'nav_id':'nav_usuarios',
        'form': form,
        'accionOk': accionOk,
        'accionReturn': accionReturn,
        }
    return render(request, 'usuario/usuario_crear.html',context=c)

class UsuarioUpdate(UpdateView):
    model = Usuario
    fields = ['documento','nombre','apellido','email','telefono','permisos','institucion']
    template_name = 'usuario/usuario_editar.html'
    success_url = reverse_lazy('usuario_editado',kwargs={'accionOk':True,'accionReturn':'Usuario editado correctamente.'})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usuario_select'] = True
        context['usuario_logueado']=True
        context['usuario']=self.request.user.username
        context['usuarios']=Usuario.objects.filter(activo=True)
        context['nav_id']='nav_usuarios'
        context['form'].fields['institucion'].queryset = Institucion.objects.filter(activo=True)
        return context

    def form_invalid(self, form):
        return reverse_lazy('usuario_editado',kwargs={'accionOk':False,'accionReturn':'Error: {}.'.format(form.errors)})

@login_required
def editar(request,accionOk=None,accionReturn=None):
    usuarios = Usuario.objects.filter(activo=True)
    
    c = {
        'usuario_logueado':True,
        'usuario':request.user.username,
        'nav_id':'nav_usuarios',
        'usuarios':usuarios,
        'accionOk':accionOk,
        'accionReturn':accionReturn,
        }
    return render(request, 'usuario/usuario_editar.html',context=c)

@login_required
def eliminar(request):
    accionOk = None
    accionReturn = None
    usuarios = Usuario.objects.filter(activo=True)

    if request.method == 'POST':
        try:
            usuario_eliminado = Usuario.objects.get(pk=int(request.POST['usuario_pk']))
            usuario_eliminado.activo = False
            usuario_eliminado.save()
            user_eliminado = User.objects.filter(username=usuario_eliminado.documento).first()
            user_eliminado.is_active = False
            user_eliminado.save()
            accionOk = True
            accionReturn = 'El usuario {} ha sido eliminado correctamente.'.format(usuario_eliminado)
        except Exception as e:
            accionOk = False
            accionReturn = "Ocurrió un error al eliminar el usuario. Error: {}".format(e) 
    c = {
        'usuario_logueado':True,
        'usuario':request.user.username,
        'nav_id':'nav_usuarios',
        'usuarios':usuarios,
        'accionOk':accionOk,
        'accionReturn':accionReturn,
        }
    return render(request, 'usuario/usuario_eliminar.html',context=c)

def password_generator(length=8):
    '''
    Generates a random password having the specified length
    :length -> length of password to be generated. Defaults to 8
        if nothing is specified.
    :returns string <class 'str'>
    '''
    LETTERS = string.ascii_letters
    NUMBERS = string.digits  
    
    # create alphanumerical from string constants
    printable = f'{LETTERS}{NUMBERS}'

    # convert printable from string to list and shuffle
    printable = list(printable)
    random.shuffle(printable)

    # generate random password and convert to string
    random_password = random.choices(printable, k=length)
    random_password = ''.join(random_password)
    return random_password