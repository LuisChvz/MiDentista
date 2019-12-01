from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Publicacion, Especialidad, Tratamiento, Medicamento, Promocion, Categoria

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
            'nombre':''
        }

class NuevoMedicamentoForm(forms.ModelForm):
    
    class Meta: 
        model = Medicamento
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre: '}),
        }
        labels = {
            'nombre':''
        }
        
class CategoriaModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, Categoria):
         return Categoria.nombre

class NuevoTratamientoForm(forms.ModelForm):
    
    categoria =  CategoriaModelChoiceField(queryset = Categoria.objects.filter().order_by('id'), required = True, widget = forms.Select(attrs={'class':'form-control'}))
    
    class Meta: 
        model = Tratamiento
        fields = ['nombre','descripcion','precio', 'categoria']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre: '}),
            'descripcion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Descripcion: '}),
            'precio': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Precio: '}),
        }
        labels = {
            'nombre':'',
            'descripcion':'',
            'precio':''
        }
        
class TratamientoModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, Tratamiento):
         return Tratamiento.nombre
     
class NuevaPromocionForm(forms.ModelForm):
    
    tratamiento =  TratamientoModelChoiceField(queryset = Tratamiento.objects.filter().order_by('id'), required = True, widget = forms.Select(attrs={'class':'form-control'}))

    
    class Meta: 
        model = Promocion
        fields = ['tratamiento', 'titulo', 'descripcion','descuento', 'image']
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título:'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Descripcion: '}),
            'descuento': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Descuento: '}),
            'image': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'})
        }
        labels = {
            'tratamiento':'',
            'titulo':'',
            'descripcion':'',
            'descuento':'Descuento' ,
            'image':'Imagen'
        }
        
    def clean_descuento(self):
        descuento = self.cleaned_data.get("descuento")
            
        if descuento >= 100:
            raise forms.ValidationError("El descuento debe ser menor al 100%")
        return descuento