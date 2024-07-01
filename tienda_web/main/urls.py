from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('formulario/',views.formulario, name='formulario'),
    path('login/',views.iniciar_sesion, name='login'),
    path('perfil/',views.perfil, name='perfil'),
    path('register/',views.register, name='register'),
    
]