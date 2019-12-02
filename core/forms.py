from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Publicacion, Especialidad, Tratamiento, Medicamento, Promocion, Categoria, Dentista, Paciente, Cita, Receta

class NuevaPublicacionForm(forms.ModelForm):
    
    image = forms.ImageField(required=True)
    
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
    image = forms.ImageField(required=True)
    class Meta: 
        model = Tratamiento
        fields = ['nombre','descripcion','precio', 'categoria', 'image']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre: '}),
            'descripcion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Descripcion: '}),
            'precio': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Precio: '}),
            'image': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'})
        }
        labels = {
            'nombre':'',
            'descripcion':'',
            'precio':'',
            'image':'Imagen'
        }
        
class TratamientoModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, Tratamiento):
         return Tratamiento.nombre
     
class NuevaPromocionForm(forms.ModelForm):
    
    tratamiento =  TratamientoModelChoiceField(queryset = Tratamiento.objects.filter().order_by('id'), required = True, widget = forms.Select(attrs={'class':'form-control'}))
    image = forms.ImageField(required=True)
    
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
    
class NuevoUserForm(UserCreationForm):
    
    class Meta: 
        model = User
        fields = ['username','first_name','last_name','email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Usuario:'}),
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombres:'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellidos:'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email: '}),

        }
        labels = {
            'username':'','first_name':'','last_name':'','email':'','password1':'','password2':''
        }

class EspecialidadModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, Especialidad):
        return Especialidad.nombre
      
class NuevoDentistaForm(forms.ModelForm):
    
    especialidad =  EspecialidadModelChoiceField(queryset = Especialidad.objects.filter().order_by('id'), required = True, widget = forms.Select(attrs={'class':'form-control'}))
    foto = forms.ImageField(required=True, label="Foto de perfil")
    class Meta: 
        model = Dentista
        fields = ['usuario','telefono', 'biografia', 'especialidad', 'foto']
        widgets = {
            'usuario': forms.HiddenInput(),
            'especialidad': forms.Select(attrs={'class':'form-control',}),
            'telefono': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Telefono: '}),
            'biografia': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Biografía: '}),
            'foto': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'})
        }
        labels = {
            'telefono':'',
            'biografia':'',
            'precio':'',
            
        }

class MedicamentoModelChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, Medicamento):
        return Medicamento.nombre
        
class NuevoPacienteForm(forms.ModelForm):
    
    alergias =  MedicamentoModelChoiceField(queryset = Medicamento.objects.filter().order_by('id'), required = True, widget = forms.SelectMultiple(attrs={'class':'form-control'}))

    foto = forms.ImageField(required=True, label="Foto de perfil")
    class Meta: 
        model = Paciente
        fields = ['nombres','apellidos', 'nacimiento', 'telefono', 'alergias', 'foto']
        widgets = {
            'nombres': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombres:'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellidos:'}),
            'telefono': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Telefono: '}),
            'nacimiento': forms.DateInput(attrs={'readonly':'true','class':'form-control datePicker','data-provide':'datepicker','data-date-end-date':'0d',"data-date-format":"dd/mm/yyyy" }),
            'foto': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'})
        }
        labels = {
            'telefono':'Telefono',
            'nombres':'',
            'apellidos':'',
            'nacimiento':'Fecha de nacimiento'
        }
        
