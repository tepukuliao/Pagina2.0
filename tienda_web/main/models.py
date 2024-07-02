from django.db import models

# Create your models here.
<<<<<<< HEAD
class Usuario(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    usuario = models.CharField(max_length=25, unique=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    correo = models.EmailField(unique=True, max_length=100)
    fecha_nacimiento = models.DateField(blank=False)
    password = models.CharField(max_length=20)

=======


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
>>>>>>> 463af8a668f2153497b9f16afc5f5d58ddaf7484
    
    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido)

<<<<<<< HEAD
    class Meta:
        verbose_name = 'Usuario '
        verbose_name_plural = 'Usuarios'


=======
>>>>>>> 463af8a668f2153497b9f16afc5f5d58ddaf7484
