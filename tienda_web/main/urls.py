from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('formulario/',views.formulario, name='formulario'),
    path('login/',views.iniciar_sesion, name='login'),
    
]