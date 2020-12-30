from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
import string
import random
from settings.local import EMAIL_HOST_USER
from modules.auxiliar.views import usuario_logueado
from .forms import UsuarioForm

@login_required
def crear(request):
    accionOk = None
    usuario_creado = None
    error = None
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
            usuario_creado = '{} {}'.format(usuario.nombre,usuario.apellido)
            try:
                send_mail(
                    'Datos de ingreso BI en Deportistas de Alto Rendimiento',
                    'Usuario: {}. Contraseña: {}'.format(usuario.documento, contraseña),
                    EMAIL_HOST_USER,
                    [usuario.email],
                    fail_silently=False,
                )
            except Exception as e:
                accionOk = False
                error = "Ocurrió un error al enviar los datos de acceso por email. Error: {}".format(e)
    form = UsuarioForm()

    c = {
        'usuario_logueado':True,
        'usuario':request.user.username,
        'form': form,
        'accionOk': accionOk,
        'usuario_creado': usuario_creado,
        'error': error,
        }
    return render(request, 'usuarios.html',context=c)

@login_required
def editar(request):
    c = {
        'usuario_logueado':True,
        'usuario':request.user.username,
        }
    return render(request, 'usuarios.html',context=c)

@login_required
def eliminar(request):
    c = {
        'usuario_logueado':True,
        'usuario':request.user.username,
        }
    return render(request, 'usuarios.html',context=c)

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