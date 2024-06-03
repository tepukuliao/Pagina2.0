from django.shortcuts import render


def index(request):
    try:
        if request.method == 'POST':
            correo = request.POST.get("correo")
            contraseña = request.POST.get("contraseña")
            print(correo)
            print(contraseña)
            return render(request,'index.html')
        elif request.method == 'GET':
            return render(request,'index.html')
    except Exception as error:
        print(error)
    