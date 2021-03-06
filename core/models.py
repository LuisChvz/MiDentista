from __future__ import unicode_literals
from django.contrib import admin
from django.core.validators import MinValueValidator
from django.db import models
import decimal
from django.contrib.auth.models import User
from datetime import date
from multiselectfield import MultiSelectField

class Especialidad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=64)

class Dentista(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=8)
    is_dentist = models.BooleanField(default=True)
    foto = models.ImageField(upload_to='dentist/%Y/%m/%D/', null=True, blank=True)
    biografia = models.CharField(max_length=1024)
    
class Medicamento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=64)
    
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=64)
    
class Tratamiento(models.Model):
    id = models.AutoField(primary_key=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=64)
    descripcion = models.CharField(max_length=512)
    precio = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    precioNeto = models.DecimalField(max_digits=6, decimal_places=2, default=0, validators=[MinValueValidator(0)],)
    image = models.ImageField(upload_to='services/%Y/%m/%D/', null=True, blank=True)
    
    def CalcularPN(self, descuento, precio, id):
        tratamiento = Tratamiento.objects.get(id=id)
        tratamiento.precioNeto = precio * (decimal.Decimal(1) - descuento/decimal.Decimal(100))
        tratamiento.save()
        
class Promocion(models.Model):
    id = models.AutoField(primary_key=True)
    tratamiento = models.ForeignKey(Tratamiento, on_delete=models.CASCADE, blank=True, null=True)
    titulo = models.CharField(max_length=64)
    descripcion = models.CharField(max_length=512)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to='promo/%Y/%m/%D/', null=True, blank=True)
    created = models.DateField(auto_now=True)

class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=64)
    apellidos = models.CharField(max_length=64)
    nacimiento = models.DateField()
    telefono = models.CharField(max_length=8)
    foto = models.ImageField(upload_to='patient/%Y/%m/%D/', null=True, blank=True)
    edad = models.IntegerField(default=0)
    alergias = models.ManyToManyField(Medicamento,  blank=True)
    correo = models.EmailField(blank=True, null=True)
    
    def calcularEdad(self, id):
        paciente = Paciente.objects.get(id=id)
        today = date.today()
        
        paciente.edad = today.year - paciente.nacimiento.year - ((today.month, today.day) < (paciente.nacimiento.month, paciente.nacimiento.day))
        paciente.save()

    
class Receta(models.Model):
    id = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medicamento = models.ManyToManyField(Medicamento)
    indicaciones = models.CharField(max_length=128)
    
class Cita(models.Model):
    id = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, blank=True, null=True)
    dentista = models.ForeignKey(Dentista, on_delete=models.CASCADE, blank=True, null=True)
    tratamiento = models.ForeignKey(Tratamiento, on_delete=models.CASCADE, null=True, blank=True)
    hora = models.TimeField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    informe = models.CharField(max_length=1024, default="No se ha agregado informe.")
    asignada = models.BooleanField(default=False)
    atendida = models.BooleanField(default=False)
    
class Publicacion(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=128)
    descripcion = models.CharField(max_length=1024)
    created = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='post/%Y/%m/%D/', null=True, blank=True)
    
    
    

admin.site.register(Publicacion)
admin.site.register(Especialidad)
admin.site.register(Dentista)
admin.site.register(Medicamento)
admin.site.register(Tratamiento)
admin.site.register(Categoria)
admin.site.register(Promocion)
admin.site.register(Paciente)
admin.site.register(Receta)
admin.site.register(Cita)