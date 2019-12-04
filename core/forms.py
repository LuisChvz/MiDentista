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
        
    def clean_first_name(self):
        first_name=self.cleaned_data.get('first_name')
        if first_name.replace(" ","").isalpha():
            return first_name
        else:
            raise forms.ValidationError("Por favor ingrese sus nombres correctamente.")

    def clean_last_name(self):
        last_name=self.cleaned_data.get('last_name')
        if last_name.replace(" ","").isalpha():
            return last_name
        else:
            raise forms.ValidationError("Por favor ingrese sus apellidos correctamente.")

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
        
        
    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if (telefono.startswith('7') | telefono.startswith('6') | telefono.startswith('2')) and telefono[1:8].isdigit() and len(telefono)==8:
            return telefono
        else:
            raise forms.ValidationError('Por favor ingrese un número de telefono valido en El Salvador.')

class MedicamentoModelChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, Medicamento):
        return Medicamento.nombre
        
class NuevoPacienteForm(forms.ModelForm):
    
    alergias =  MedicamentoModelChoiceField(queryset = Medicamento.objects.filter().order_by('id'), widget = forms.SelectMultiple(attrs={'class':'form-control'}))

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
        
    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if (telefono.startswith('7') | telefono.startswith('6') | telefono.startswith('2')) and telefono[1:8].isdigit() and len(telefono)==8:
            return telefono
        else:
            raise forms.ValidationError('Por favor ingrese un número de telefono valido en El Salvador.')
        
    def clean_nombres(self):
        nombres=self.cleaned_data.get('nombres')
        if nombres.replace(" ","").isalpha():
            return nombres
        else:
            raise forms.ValidationError("Por favor ingrese sus nombres correctamente.")

    def clean_apellidos(self):
        apellidos=self.cleaned_data.get('apellidos')
        if apellidos.replace(" ","").isalpha():
            return apellidos
        else:
            raise forms.ValidationError("Por favor ingrese sus apellidos correctamente.")
        
class NuevaCategoriaForm(forms.ModelForm):
    
    class Meta: 
        model = Categoria
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre: '}),
        }
        labels = {
            'nombre':''
        }
        
class CitaForm(forms.ModelForm):
    
    fecha = forms.DateField(required=True, widget=forms.DateInput(attrs={'readonly':'true', 'required':'True','class':'form-control datePicker','data-provide':'datepicker','data-date-end-date':'0d',"data-date-format":"dd/mm/yyyy" }))
    
    class Meta: 
        model = Cita
        fields = ['fecha']
        widgets = {
            
            'fecha': forms.DateInput(attrs={'readonly':'true', 'required':'True','class':'form-control datePicker','data-provide':'datepicker','data-date-end-date':'0d',"data-date-format":"dd/mm/yyyy" }),
        
        }
        labels = {

            'fecha':'Fecha'
        }
        
    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')
        
        if Cita.objects.filter(fecha = fecha).exists():
            raise forms.ValidationError('Ya hay citas habilitadas para esta fecha.')
        else:
            return fecha
        
        
class NuevaRecetaForm(forms.ModelForm):
    
    medicamento =  MedicamentoModelChoiceField(queryset = Medicamento.objects.filter().order_by('id'), widget = forms.SelectMultiple(attrs={'class':'form-control'}))
    class Meta: 
        model = Receta
        fields = ['paciente','medicamento', 'indicaciones']
        widgets = {
            'paciente': forms.HiddenInput(),
            'indicaciones': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Indicaciones:'}),
        }
        labels = {
            'indicaciones':'Indicaciones',
        }
        

class UpdateCitaForm(forms.ModelForm):
    
    tratamiento =  TratamientoModelChoiceField(required = True, queryset = Tratamiento.objects.filter().order_by('id'), widget = forms.Select(attrs={'class':'form-control'}))

    class Meta: 
        model = Cita
        fields = ['informe','tratamiento', 'atendida']
        widgets = {
            'informe': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Biografía: '}),
            'atendida': forms.HiddenInput()
        }
        labels = {
            'informe':'',
        }