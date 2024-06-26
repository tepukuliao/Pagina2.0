from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib import messages
from django.db import IntegrityError
from .models import Usuario
from django.contrib.auth.hashers import make_password, check_password


def index(request):
    return render(request,'index.html', {'usuario':request.user})
    

def formulario(request):
    if request.method == 'GET':

        return render(request,'formulario.html')
    else:

        rut = request.POST.get('rut')
        usuario = request.POST.get('usuario')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        fecha_nacimiento = request.POST.get('fechaNac')
        telefono = request.POST.get('fono')
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        print(usuario, nombre, correo, telefono, password1)
        if password1 != password2:
            error_message = "Las contraseñas no coinciden."
            return render(request, 'formulario.html', {'error_message': error_message})

        try:
            usuario = Usuario.objects.create(
                rut = rut,
                usuario = usuario,
                nombre = nombre,
                apellido = apellido,
                correo = correo,
                fecha_nacimiento = fecha_nacimiento,
                telefono = telefono,
                password = make_password(password1),
                activo = True
            )
            return render(request,'login.html')
        except IntegrityError as error:
            print(error)
            error_message = "El correo electrónico ya existe."
            return render(request,'formulario.html', {'error_message': error_message})



def iniciar_sesion(request):
    try:

        if request.method == 'POST':
            usuario = request.POST.get("usuario")
            password = request.POST.get("password")
            print(usuario, password)
            User = get_user_model()
            try:
                user = User.objects.get(username=usuario)
            except User.DoesNotExist:
                user = None

            if user is None:
                error_message = 'El usuario ingresado no esta registrado'
                return render(request,'login.html', {'error_message': error_message}) 
            else: 
                user = authenticate(username=usuario, password=password)
                if user is not None:
                    login(request,user)
                    return redirect('inicio')
                else:
                    error_message = 'usuario o contraseña incorrecta'
                    return render(request,'login.html', {'error_message': error_message}) 

        else:
            return render(request,'login.html') 
    except Exception as error:
        print(error)
        return render(request,'login.html') 
   
   

   
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



    