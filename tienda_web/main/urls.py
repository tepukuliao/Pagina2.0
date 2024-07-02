from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('formulario/',views.formulario, name='formulario'),
    path('login/',views.iniciar_sesion, name='login'),
    path('perfil/',views.perfil, name='perfil'),
<<<<<<< HEAD
    path('cerrar_sesion/', views.cerrar_sesion, name='logout'),
=======
    path('register/',views.register, name='register'),
>>>>>>> 463af8a668f2153497b9f16afc5f5d58ddaf7484
    
]