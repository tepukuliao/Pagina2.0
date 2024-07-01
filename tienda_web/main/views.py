from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib import messages
from django.db import IntegrityError
from .models import Usuario
from django.contrib.auth.hashers import make_password, check_password


def index(request):
    return render(request,'index.html')
    

def formulario(request):
    if request.method == 'GET':

        return render(request,'formulario.html')
    else:
        
        rut = request.POST.get('rut')
        username = request.POST.get('username')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        fecha_nacimiento = request.POST.get('fechaNac')
        telefono = request.POST.get('telefono')
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")


        print(request.POST)
        print(username, nombre, correo, telefono, password1)


        if password1 != password2:
            error_message = "Las contraseñas no coinciden."
            return render(request, 'formulario.html', {'error_message': error_message})

        try:
            usuario = Usuario.objects.create(
                rut = rut,
                username = username,
                nombre = nombre,
                apellido = apellido,
                correo = correo,
                fecha_nacimiento = fecha_nacimiento,
                telefono = telefono,
                password = password1,
                activo = True
            )
            usuario.save()
            return redirect('login')
        except IntegrityError as error:
            print(error)
            return render(request,'formulario.html')


def register(request):
    return render(request, 'registration/register.html')



def iniciar_sesion(request):

        if request.method == 'POST':
            username = request.POST.get("username")
            password = request.POST.get("password")
            print(request.POST)
            print(username, password)
            User = get_user_model(Usuario)
            try:
                user = User.objects.get(username=username)
            except Usuario.DoesNotExist:
                user = None
               
            if user is None:
                error_message = 'El usuario ingresado no esta registrado'
                return render(request,'login.html', {'error_message': error_message}) 
            else: 
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request,user)
                    return redirect('inicio')
                else:
                    error_message = 'usuario o contraseña incorrecta'
                    return render(request,'login.html', {'error_message': error_message}) 

        else:
            return render(request,'login.html') 

   
@login_required
def perfil(request):
    perfil = Usuario.objects.all()
    return render(request,'perfil.html')



    