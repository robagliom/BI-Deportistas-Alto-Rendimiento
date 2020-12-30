from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from . import views
from modules.usuario.models import Usuario

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