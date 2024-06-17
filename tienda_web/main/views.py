from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.db import IntegrityError
import requests


def index(request):
    return render(request,'index.html', {'usuario':request.user})
    

def formulario(request):
    try:
        if request.method == "POST":
            nombre = request.POST.get("nombre") 
            apellido = request.POST.get("apellido")
            usuario = request.POST.get("usuario")
            correo = request.POST.get("correo")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")
            print(nombre,apellido,usuario,correo,password1,password2)
            if password1 == password2:
                user = User.objects.create_user(first_name=nombre, last_name=apellido, username=usuario, email=correo, password=password1)
                user.save()
                return render(request,'login.html')
            else:
                return render(request,'formulario.html',
                {'mensaje':'Las contraseñas no coinciden'})
        elif request.method == 'GET':
            return render(request,'formulario.html')

    except IntegrityError as valorUnico:
        print(valorUnico)
        return render(request,'formulario.html',{'mensaje':'Usuario ya existe'})
    except Exception as error:
        print(error)
        return render(request, 'formulario.html', {'error': 'Ha ocurrido un error inesperado. Por favor, inténtelo de nuevo.'})


def iniciar_sesion(request):
    try:
        if request.method == "POST":
            usuario = request.POST.get("usuario")
            password = request.POST.get("password")
            print(usuario,password)
            user = authenticate(request, username=usuario, password=password)
            login(request,user)
            return render(request,'index.html')
        elif request.method == 'GET':
            return render(request,'login.html')
    except Exception as error:
        print(error)
        return render(request, 'login.html', {'error': 'Ha ocurrido un error inesperado. Por favor, inténtelo de nuevo.'})


def perfil(request):
    return render(request,'perfil.html')


def home(request):
    url = url
    response = requests.get(url)
    