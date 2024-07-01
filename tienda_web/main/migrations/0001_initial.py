# Generated by Django 5.0.6 on 2024-06-30 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=25, unique=True)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('correo', models.EmailField(max_length=100, unique=True)),
                ('fecha_nacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=40, null=True)),
                ('password', models.CharField(max_length=20)),
                ('activo', models.BooleanField()),
            ],
        ),
    ]
