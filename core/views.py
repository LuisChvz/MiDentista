from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from braces.views import SuperuserRequiredMixin, LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from .models import Publicacion, Especialidad, Tratamiento, Medicamento, Promocion, Dentista, Paciente, Categoria
from .forms import NuevaPublicacionForm, NuevoMedicamentoForm, NuevaEspecialidadForm, NuevoTratamientoForm, NuevaPromocionForm
from .forms import NuevoUserForm, NuevoDentistaForm, NuevoPacienteForm, NuevaCategoriaForm
from django import forms
from django.contrib.auth.decorators import login_required, user_passes_test


def home(request):
    promociones = Promocion.objects.filter().order_by('-id')[:5]
    cantidad = Promocion.objects.filter().count()
    post = Publicacion.objects.all().order_by('-id')
    ps = []
    i=0
    for p in promociones:
        ps.append(p)
        i = i + 1
        
    if cantidad > 0:
        p0 = ps[0]
        if cantidad > 1:
            p1 = ps[1]
            if cantidad > 2:
                p2 = ps[2]
                if cantidad > 3:
                    p3 = ps[3]
                    if cantidad > 4:
                        p4 = ps[4]
                        
    if cantidad == 1:
        return render(request, "core/home.html", {'p0':p0, 'cantidad':cantidad, 'post':post})
    elif cantidad == 2:
        return render(request, "core/home.html", {'p0':p0, 'p1':p1, 'cantidad':cantidad, 'post':post})
    elif cantidad == 3:
        return render(request, "core/home.html", {'p0':p0, 'p1':p1, 'p2':p2, 'cantidad':cantidad, 'post':post})
    elif cantidad == 4:
        return render(request, "core/home.html", {'p0':p0, 'p1':p1, 'p2':p2, 'p3':p3, 'cantidad':cantidad, 'post':post})
    elif cantidad == 5:
        return render(request, "core/home.html", {'p0':p0, 'p1':p1, 'p2':p2, 'p3':p3, 'p4':p4, 'cantidad':cantidad, 'post':post})
    else:
        return render(request, "core/home.html", {'post':post})
    

class NuevaPublicacion(SuperuserRequiredMixin, CreateView):
    model = Publicacion
    form_class = NuevaPublicacionForm
    success_url = reverse_lazy('home')
    
@user_passes_test(lambda u: u.is_superuser)
def Blog(request):
    promociones = Promocion.objects.all()
    publicaciones = Publicacion.objects.all()
    
    return render(request, "core/blog.html", {'publicaciones':publicaciones, 'promociones':promociones})
    
    
class NuevaEspecialidad(SuperuserRequiredMixin, CreateView):
    model = Especialidad
    form_class = NuevaEspecialidadForm
    success_url = reverse_lazy('home')

class NuevoMedicamento(SuperuserRequiredMixin, CreateView):
    model = Medicamento
    form_class = NuevoMedicamentoForm
    success_url = reverse_lazy('home')    
    
@user_passes_test(lambda u: u.is_superuser)
def NuevoTratamiento(request):
    if request.method == 'POST':
        form = NuevoTratamientoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            ultimo = Tratamiento.objects.latest('id')
            
            instancia = Tratamiento()
            
            instancia.CalcularPN(0, ultimo.precio, ultimo.id)   
            
            return redirect('home')
    else:
        form = NuevoTratamientoForm()
    
    return render(request, 'core/tratamiento_form.html', {'form':form})

@user_passes_test(lambda u: u.is_superuser)
def NuevaPromocion(request):
    if request.method == 'POST':
        form = NuevaPromocionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            ultima = Promocion.objects.latest('id')
            
            instancia = Tratamiento()
            instancia.CalcularPN(ultima.descuento, ultima.tratamiento.precio, ultima.tratamiento.id)
            
            return redirect('home')
    else:
        form = NuevaPromocionForm()
    
    return render(request, 'core/promocion_form.html', {'form':form})


class TratamientoList(ListView):
    model = Tratamiento
    template_name = 'core/tratamiento_list.html'

class MedicamentoList(LoginRequiredMixin, ListView):
    model = Medicamento
    template_name = 'core/medicamento_list.html'

class EspecialidadList(LoginRequiredMixin, ListView):
    model = Especialidad
    template_name = 'core/especialidad_list.html'

class TratamientoUpdate(SuperuserRequiredMixin, UpdateView):
    model = Tratamiento
    template_name = 'core/tratamiento_update.html'
    form_class = NuevoTratamientoForm
    success_url = reverse_lazy('core:tratamientos')

class MedicamentoUpdate(SuperuserRequiredMixin, UpdateView):
    model = Medicamento
    template_name = 'core/medicamento_update.html'
    form_class = NuevoMedicamentoForm
    success_url = reverse_lazy('core:medicamentos')

class EspecialidadUpdate(SuperuserRequiredMixin, UpdateView):
    model = Especialidad
    template_name = 'core/especialidad_update.html'
    form_class = NuevaEspecialidadForm
    success_url = reverse_lazy('core:especialidades')

class TratamientoDelete(SuperuserRequiredMixin, DeleteView):
    model = Tratamiento
    template_name= "core/tratamiento_delete.html"
    success_url = reverse_lazy('core:tratamientos')


class MedicamentoDelete(SuperuserRequiredMixin, DeleteView):
    model = Medicamento
    template_name= "core/medicamento_delete.html"
    success_url = reverse_lazy('core:medicamentos')

class EspecialidadDelete(SuperuserRequiredMixin, DeleteView):
    model = Especialidad
    template_name= "core/especualidad_delete.html"
    success_url = reverse_lazy('core:especialidades')
    
class NuevoUsuario(SuperuserRequiredMixin, CreateView):
    model = User
    form_class = NuevoUserForm
    template_name = 'core/user_form.html'
    
    def get_success_url(self):
        return reverse_lazy('core:nuevodentista', args=[self.object.id])
    
    def get_form(self, form_class = None):
        form = super(NuevoUsuario, self).get_form()

        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contraseña: '})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Confirmar contraseña: '})
        return form

@user_passes_test(lambda u: u.is_superuser)
def NuevoDentista(request, usuario):
    if request.method == 'POST':
        form = NuevoDentistaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return redirect('home')
            
    else:
        form = NuevoDentistaForm()
        form.initial['usuario'] = usuario
    
    return render(request, 'core/dentista_form.html', {'form':form})

class UpdateUsuario(SuperuserRequiredMixin, UpdateView):
    model = User
    form_class = NuevoUserForm
    template_name = 'core/user_update.html'
    
    def get_success_url(self):
        return reverse_lazy('core:updatedentista', args=[self.object.id])
    
class UpdateDentista(SuperuserRequiredMixin, UpdateView):
    model = Dentista
    form_class = NuevoDentistaForm
    template_name = 'core/dentista_update.html'
    success_url = reverse_lazy('home')
    
class ModificarPublicacion(SuperuserRequiredMixin, UpdateView):
    model = Publicacion
    form_class = NuevaPublicacionForm
    template_name = 'core/publicacion_update.html'
    success_url = reverse_lazy('core:blog')


class EliminarPublicacion(SuperuserRequiredMixin, DeleteView):
    model = Publicacion
    template_name = 'core/publicacion_delete.html'
    def get_success_url(self):
        return reverse_lazy('core:blog')

class ListaPromocion(SuperuserRequiredMixin, ListView):
    model = Promocion

class ModificarPromocion(SuperuserRequiredMixin, UpdateView):
    model = Promocion 
    form_class = NuevaPromocionForm
    template_name = 'core/promocion_update.html'
    success_url = reverse_lazy('core:blog')

class EliminarPromocion(SuperuserRequiredMixin, DeleteView):
    model = Promocion
    template_name = 'core/promocion_delete.html'
    def get_success_url(self):
        return reverse_lazy('core:blog')
    

@user_passes_test(lambda u: u.is_superuser)
def NuevoPaciente(request):
    if request.method == 'POST':
        form = NuevoPacienteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            ultimo = Paciente.objects.latest('id').id
            instancia = Paciente()
            
            instancia.calcularEdad(ultimo)

            return redirect('home')
            
    else:
        form = NuevoPacienteForm()
        
    return render(request, 'core/paciente_form.html', {'form':form})
            

class DentistaList(ListView):
    model = Dentista
    template_name = 'core/dentista_list.html'
       
            
class DentistaDelete(SuperuserRequiredMixin, DeleteView):
    model = Dentista
    template_name= "core/dentista_delete.html"
    success_url = reverse_lazy('core:dentistas')

class PacienteList(LoginRequiredMixin, ListView):
    model = Paciente
    template_name = 'core/paciente_list.html'

class PacienteDelete(SuperuserRequiredMixin, DeleteView):
    model = Paciente
    template_name= "core/paciente_delete.html"
    success_url = reverse_lazy('core:pacientes')
    
    
class NuevaCategoria(SuperuserRequiredMixin, CreateView):
    model = Categoria
    form_class = NuevaCategoriaForm
    success_url = reverse_lazy('core:categorias')  

class CategoriaList(ListView):
    model = Categoria
    template_name = 'core/categoria_list.html'   

class CategoriaUpdate(LoginRequiredMixin, UpdateView):
    model = Categoria
    template_name = 'core/categoria_update.html'
    form_class = NuevaCategoriaForm
    success_url = reverse_lazy('core:categorias') 

class CategoriaDelete(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name= "core/categoria_delete.html"
    success_url = reverse_lazy('core:categorias')
    
def ReestablecerPrecio(request, pk):
    tratamiento = Tratamiento.objects.get(id=pk)
    tratamiento.precioNeto = tratamiento.precio
    tratamiento.save()
    return redirect('core:tratamientos')

    