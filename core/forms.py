from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Publicacion

class NuevaPublicacionForm(forms.ModelForm):
    
    class Meta: 
        model = Publicacion
        fields = ['titulo','descripcion']
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre: '}),
            'descripcion': forms.Textarea(attrs={'class':'form-control'}),
            
        }
        labels = {
            'nombre':'Nombre'
        }
