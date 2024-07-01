from django.db import models

# Create your models here.


class Usuario(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    username = models.CharField(max_length=25, unique=True)
    nombre = models.CharField(max_length=20, null=False)
    apellido = models.CharField(max_length=20, null=False)
    correo = models.EmailField(unique=True, max_length=100, null=False)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    telefono = models.CharField(max_length=40, null=True)
    password = models.CharField(max_length=20)
    activo = models.BooleanField()
    
    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido)

