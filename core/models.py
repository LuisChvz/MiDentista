from __future__ import unicode_literals
from django.core.validators import MinValueValidator
from django.db import models
import decimal
from django.contrib.auth.models import User

class Especializacion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=64)

class Dentista(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    especializacion = models.ForeignKey(Especializacion, on_delete=models.CASCADE)
    telefono = models.IntegerField()
    correo = models.EmailField(unique=True)
    
class Medicamento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=64)
    
class Tratamiento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=64)
    descripcion = models.CharField(max_length=512)
    precio = models.DecimalField(max_digits=3, decimal_places=2)
    descuento = models.DecimalField(max_digits=2, decimal_places=2)
    precioNeto = models.DecimalField(max_digits=3, decimal_places=2)
    
class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=64)
    apellidos = models.CharField(max_length=64)
    nacimiento = models.DateField()
    telefono = models.IntegerField()
    correo = models.EmailField(unique=True)
    
class Alergia(models.Model):
    id = models.AutoField(primary_key=True)
    alergia = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    
class Receta(models.Model):
    id = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    indicaciones = models.CharField(max_length=128)
    
class Cita(models.Model):
    id = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    dentista = models.ForeignKey(Dentista, on_delete=models.CASCADE)
    tratamiento = models.ForeignKey(Tratamiento, on_delete=models.CASCADE)
    hora = models.TimeField()
    fecha = models.DateField()
    informe = models.CharField(max_length=1024)
    
class Publicacion(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=128)
    descripcion = models.CharField(max_length=512)
    created = models.DateField(auto_now=True)
    image = models.ImageField()
    