from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.db import IntegrityError
from .models import Usuario


def index(request):
    return render(request,'index.html', {'usuario':request.user})
    

def formulario(request):
    if request.method == 'GET':

        return render(request,'formulario.html')
    else:
        print("metodo post")
        rut = request.POST.get('rut')
        usuario = request.POST.get('usuario')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        fecha_nacimiento = request.POST.get('fechaNac')
        telefono = request.POST.get('fono')

        try:
            usuario = Usuario.objects.create(
                rut = rut,
                usuario = usuario,
                nombre = nombre,
                apellido = apellido,
                correo = correo,
                fecha_nacimiento = fecha_nacimiento,
                telefono = telefono,
                activo = True
            )
            return render(request,'formulario.html')
        except IntegrityError as error:
            print(error)
            # El correo electrónico ya existe en la base de datos
            error_message = "El correo electrónico ya existe en la base de datos. Por favor, ingresa un correo electrónico diferente."
            return render(request,'formulario.html', {'error_message': error_message})



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



    