from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Publicacion, Especialidad, Tratamiento, Medicamento

class NuevaPublicacionForm(forms.ModelForm):
    
    class Meta: 
        model = Publicacion
        fields = ['titulo','descripcion', 'image']
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título:'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descripcion: '}),
            'image': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'})
            
        }
        labels = {
            'titulo':'', 'descripcion':'', 'image':'Imagen'
        }
        
class NuevaEspecialidadForm(forms.ModelForm):
    
    class Meta: 
        model = Especialidad
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre: '}),
        }
        labels = {
            'nombre':'Nombre'
        }

class NuevoMedicamentoForm(forms.ModelForm):
    
    class Meta: 
        model = Medicamento
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre: '}),
        }
        labels = {
            'nombre':'Nombre'
        }

class NuevoTratamientoForm(forms.ModelForm):
    
    class Meta: 
        model = Tratamiento
        fields = ['nombre','descripcion','precio']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre: '}),
            'descripcion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Descripcion: '}),
            'precio': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Precio: '}),
        }
        labels = {
            'nombre':'Nombre',
            'descripcion':'Descripcion',
            'precio':'Precio'
        }