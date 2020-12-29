from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from . import views

def index(request):
    usuario_logueado = False
    usuario = None

    if request.user.is_authenticated:
        usuario_logueado = True
        usuario = request.user.username

    c = {
            'usuario_logueado':usuario_logueado,
            'usuario':usuario,
         }
    return render(request, 'index.html',context=c)

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