from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import string
import random
from modules.auxiliar.views import usuario_logueado
from .forms import UsuarioForm

@login_required
def crear(request):
    accionOk = False
    usuario_creado = None
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            accionOk = True
            usuario = form.save(commit=False)
            usuario.contraseña = password_generator()
            usuario.save()
            user = User.objects.create_user(usuario.documento,usuario.email,usuario.contraseña)
            user.save()
            usuario_creado = usuario.nombre
            #TODO: enviar por mail la contraseña
    form = UsuarioForm()

    c = {
        'usuario_logueado':True,
        'usuario':request.user.username,
        'form': form,
        'accionOk': accionOk,
        'usuario_creado': usuario_creado,
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