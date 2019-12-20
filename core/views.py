from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from braces.views import SuperuserRequiredMixin, LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from .models import Publicacion, Especialidad, Tratamiento, Medicamento, Promocion, Dentista, Paciente, Categoria, Cita, Receta
from .forms import NuevaPublicacionForm, NuevoMedicamentoForm, NuevaEspecialidadForm, NuevoTratamientoForm, NuevaPromocionForm
from .forms import NuevoUserForm, NuevoDentistaForm, NuevoPacienteForm, NuevaCategoriaForm, CitaForm, NuevaRecetaForm, UpdateCitaForm
from django import forms
from django.contrib.auth.decorators import login_required, user_passes_test
import datetime


def home(request):
    dentistas = Dentista.objects.all()
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
        return render(request, "core/home.html", {'p0':p0, 'cantidad':cantidad, 'post':post, 'dentista_list':dentistas})
    elif cantidad == 2:
        return render(request, "core/home.html", {'p0':p0, 'p1':p1, 'cantidad':cantidad, 'post':post, 'dentista_list':dentistas})
    elif cantidad == 3:
        return render(request, "core/home.html", {'p0':p0, 'p1':p1, 'p2':p2, 'cantidad':cantidad, 'post':post, 'dentista_list':dentistas})
    elif cantidad == 4:
        return render(request, "core/home.html", {'p0':p0, 'p1':p1, 'p2':p2, 'p3':p3, 'cantidad':cantidad, 'post':post, 'dentista_list':dentistas})
    elif cantidad == 5:
        return render(request, "core/home.html", {'p0':p0, 'p1':p1, 'p2':p2, 'p3':p3, 'p4':p4, 'cantidad':cantidad, 'post':post, 'dentista_list':dentistas})
    else:
        return render(request, "core/home.html", {'post':post, 'dentista_list':dentistas})
    

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
    success_url = reverse_lazy('core/especialidad')

class NuevoMedicamento(SuperuserRequiredMixin, CreateView):
    model = Medicamento
    form_class = NuevoMedicamentoForm
    success_url = reverse_lazy('core/medicamentos')    
    
@user_passes_test(lambda u: u.is_superuser)
def NuevoTratamiento(request):
    if request.method == 'POST':
        form = NuevoTratamientoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            ultimo = Tratamiento.objects.latest('id')
            
            instancia = Tratamiento()
            
            instancia.CalcularPN(0, ultimo.precio, ultimo.id)   
            
            return redirect('core:tratamientos',0,2)
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


def TratamientoList(request, categoria, orden):
    filtro = categoria
    dentistas = Dentista.objects.all()
    
    order='nombre'
    if orden==0:
        order = 'precioNeto'
    elif orden==1:
        order = "-precioNeto"
    elif orden==2:
        order = "nombre"
        
    categorias = Categoria.objects.all()
    
    if filtro == 0:
        tratamientos = Tratamiento.objects.filter().order_by(order)
    else:
        tratamientos = Tratamiento.objects.filter(categoria = filtro).order_by(order)
    
    return render(request, "core/tratamiento_list.html", {'tratamientos':tratamientos, 'categorias':categorias, 'filtro':filtro, 'dentista_list':dentistas})
    

class MedicamentoList(LoginRequiredMixin, ListView):
    model = Medicamento
    template_name = 'core/medicamento_list.html'
    
    def get_queryset(self):
        busqueda = self.request.GET.get('buscador', '')
        print(busqueda)
        if busqueda:
            queryset = Medicamento.objects.filter(nombre__istartswith = busqueda)|Medicamento.objects.filter(id__istartswith = busqueda)
            return queryset
        else:
            queryset = Medicamento.objects.all()
            return queryset

class EspecialidadList(LoginRequiredMixin, ListView):
    model = Especialidad
    template_name = 'core/especialidad_list.html'

class TratamientoUpdate(SuperuserRequiredMixin, UpdateView):
    model = Tratamiento
    template_name = 'core/tratamiento_update.html'
    form_class = NuevoTratamientoForm
    success_url = reverse_lazy('core:tratamientos', args=[0, 2])

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
    success_url = reverse_lazy('core:tratamientos', args=[0, 2])


class MedicamentoDelete(SuperuserRequiredMixin, DeleteView):
    model = Medicamento
    template_name= "core/medicamento_delete.html"
    success_url = reverse_lazy('core:medicamentos')

class EspecialidadDelete(SuperuserRequiredMixin, DeleteView):
    model = Especialidad
    template_name= "core/especialidad_delete.html"
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
            
            return redirect('core:dentistas',0)
            
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
    success_url = reverse_lazy('core:dentistas', args=[0])
    
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

            return redirect('core:pacientes')
            
    else:
        form = NuevoPacienteForm()
        
    return render(request, 'core/paciente_form.html', {'form':form})
            

def DentistaList(request, especialidad):
    filtro = especialidad
    dentistas2 = Dentista.objects.all()
        
    especialidades = Especialidad.objects.all()
    
    if filtro == 0:
        dentistas = Dentista.objects.filter()
    else:
        dentistas = Dentista.objects.filter(especialidad = especialidad)
    
    return render(request, "core/dentista_list.html", {'dentistas':dentistas, 'especialidades':especialidades, 'filtro':filtro, 'dentista_list':dentistas2})
       
            
class DentistaDelete(SuperuserRequiredMixin, DeleteView):
    model = User
    template_name= "core/dentista_delete.html"
    success_url = reverse_lazy('core:dentistas', args=[0])

class PacienteList(SuperuserRequiredMixin, ListView):
    model = Paciente
    template_name = 'core/paciente_list.html'
    
    def get_queryset(self):
        busqueda = self.request.GET.get('buscador', '')
        print(busqueda)
        if busqueda:
            queryset = Paciente.objects.filter(nombres__istartswith = busqueda)|Paciente.objects.filter(apellidos__istartswith = busqueda)|Paciente.objects.filter(id__istartswith = busqueda)
            return queryset
        else:
            queryset = Paciente.objects.all()
            return queryset
    
class PacienteList2(SuperuserRequiredMixin, ListView):
    model = Paciente
    template_name = 'core/paciente2_list.html'
    
    def get_queryset(self):
        busqueda = self.request.GET.get('buscador', '')
        print(busqueda)
        if busqueda:
            queryset = Paciente.objects.filter(nombres__istartswith = busqueda)|Paciente.objects.filter(apellidos__istartswith = busqueda)|Paciente.objects.filter(id__istartswith = busqueda)
            return queryset
        else:
            queryset = Paciente.objects.all()
            return queryset    

class PacienteList3(LoginRequiredMixin, ListView):
    model = Paciente
    template_name = 'core/paciente3_list.html'

    def get_queryset(self):
        busqueda = self.request.GET.get('buscador', '')
        print(busqueda)
        if busqueda:
            queryset = Paciente.objects.filter(nombres__istartswith = busqueda)|Paciente.objects.filter(apellidos__istartswith = busqueda)|Paciente.objects.filter(id__istartswith = busqueda)
            return queryset
        else:
            queryset = Paciente.objects.all()
            return queryset
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dentista_list'] = Dentista.objects.all()
        return context

class PacienteDelete(SuperuserRequiredMixin, DeleteView):
    model = Paciente
    template_name= "core/paciente_delete.html"
    success_url = reverse_lazy('core:pacientes')
    
    
@user_passes_test(lambda u: u.is_superuser)
def PacienteUpdate(request, pk):
    paciente = Paciente.objects.get(id=pk)
    if request.method == 'POST':
        form = NuevoPacienteForm(request.POST, request.FILES)
        if form.is_valid():
            
            paciente.nombres = form.cleaned_data['nombres']
            paciente.apellidos = form.cleaned_data['apellidos']
            paciente.nacimiento = form.cleaned_data['nacimiento']
            paciente.telefono = form.cleaned_data['telefono']
            paciente.foto = form.cleaned_data['foto']
            paciente.alergias.set(form.cleaned_data['alergias']) 
            paciente.correo = form.cleaned_data['correo']
            paciente.save()
            
            Paciente().calcularEdad(pk)

            return redirect('core:pacientes')
            
    else:
        form = NuevoPacienteForm(instance=paciente)
        
        
    return render(request, 'core/paciente_form.html', {'form':form})
    
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
    return redirect('core:tratamientos', 0,2)

@user_passes_test(lambda u: u.is_superuser)
def HabilitarCitas(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            dentistas = Dentista.objects.all()
            
            for d in dentistas:
                Cita.objects.create(
                    dentista = d,
                    hora = '8:00:00',
                )
                Cita.objects.create(
                    dentista = d,
                    hora = '9:00:00',
                )
                Cita.objects.create(
                    dentista = d,
                    hora = '10:00:00',
                )
                Cita.objects.create(
                    dentista = d,
                    hora = '11:00:00',
                )
                Cita.objects.create(
                    dentista = d,
                    hora = '14:00:00',
                )
                Cita.objects.create(
                    dentista = d,
                    hora = '15:00:00',
                )
                Cita.objects.create(
                    dentista = d,
                    hora = '16:00:00',
                )
                Cita.objects.create(
                    dentista = d,
                    hora = '17:00:00',
                )
                
                citas = Cita.objects.filter().order_by('-id')[:8]
                
                for c in citas:
                    c.fecha = form.cleaned_data['fecha']
                    c.save()
                
 
            
            return redirect('core:citas2')
            
    else:
        form = CitaForm()
        
    return render(request, 'core/cita_form.html', {'form':form})


@user_passes_test(lambda u: u.is_superuser)
def CitaList(request, paciente):
    citas = Cita.objects.filter(asignada = False, fecha = datetime.datetime.today()).order_by('fecha', 'hora')|Cita.objects.filter(asignada = False, fecha = datetime.datetime.today() + datetime.timedelta(days = 1)).order_by('fecha', 'hora')|Cita.objects.filter(asignada = False, fecha = datetime.datetime.today() + datetime.timedelta(days = 2)).order_by('fecha', 'hora')|Cita.objects.filter(asignada = False, fecha = datetime.datetime.today() + datetime.timedelta(days = 3)).order_by('fecha', 'hora')|Cita.objects.filter(asignada = False, fecha = datetime.datetime.today() + datetime.timedelta(days = 4)).order_by('fecha', 'hora')|Cita.objects.filter(asignada = False, fecha = datetime.datetime.today() + datetime.timedelta(days = 5)).order_by('fecha', 'hora')
    hoy = datetime.date.today()
    paciente = paciente
    
    return render(request, 'core/cita_list.html', {'citas':citas, 'paciente':paciente, 'hoy':hoy})

@user_passes_test(lambda u: u.is_superuser)
def CitaList2(request):
    citas = Cita.objects.filter(atendida = False, fecha = datetime.datetime.today()).order_by('fecha', 'hora')|Cita.objects.filter(atendida = False, fecha = datetime.datetime.today() + datetime.timedelta(days = 1)).order_by('fecha', 'hora')
    
    return render(request, 'core/cita_list2.html', {'citas':citas})
@login_required
def CitaList4(request):
    citas = Cita.objects.filter(asignada = True, fecha = datetime.datetime.today()).order_by('fecha', 'hora')|Cita.objects.filter(asignada = True, fecha = datetime.datetime.today() + datetime.timedelta(days = 1)).order_by('fecha', 'hora')
    dentistas = Dentista.objects.all()
    
    return render(request, 'core/cita_list4.html', {'citas':citas, 'dentista_list':dentistas})

class CitaList3(LoginRequiredMixin, ListView):
    model = Cita
    template_name = 'core/cita_list3.html'
    
    def get_queryset(self):
        return Cita.objects.filter(paciente = self.kwargs['paciente']).order_by('-fecha')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dentista_list'] = Dentista.objects.all()
        context['paciente'] = Paciente.objects.get(id=self.kwargs['paciente'])
        return context

@user_passes_test(lambda u: u.is_superuser)
def ReservarCita(request, paciente, pk):
    cita = Cita.objects.get(id=pk)
    
    cita.paciente = Paciente.objects.get(id=paciente)
    cita.asignada = True
    cita.save()

    return redirect('core:citas2')

class CitaDelete(SuperuserRequiredMixin, DeleteView):
    model = Cita
    template_name= "core/cita_delete.html"
    success_url = reverse_lazy('core:citas2')
    
@login_required
def Expediente(request, pk):
    paciente = Paciente.objects.get(id=pk)
    dentistas = Dentista.objects.all()
    
    return render(request, 'core/expediente.html', {'paciente':paciente, 'dentista_list':dentistas})

class NuevaReceta(LoginRequiredMixin, CreateView):
    model = Receta
    form_class = NuevaRecetaForm

    def get_success_url(self):
        return reverse_lazy('core:expediente', args=[self.object.paciente.id])

    def get_initial(self):
        return {
            'paciente':self.kwargs['paciente'],
        }
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dentista_list'] = Dentista.objects.all()
        context['paciente'] = Paciente.objects.get(id=self.kwargs['paciente'])
        return context

class RecetaList(LoginRequiredMixin, ListView):
    model = Receta
    def get_queryset(self):
        return Receta.objects.filter(paciente = self.kwargs['paciente']).order_by('medicamento')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dentista_list'] = Dentista.objects.all()
        context['paciente'] = Paciente.objects.get(id=self.kwargs['paciente'])
        return context

class RecetaDelete(LoginRequiredMixin, DeleteView):
    model = Receta
    template_name= "core/categoria_delete.html"
    success_url = reverse_lazy('home')
    

def CitaUpdate(request, pk):
    cita = Cita.objects.get(id=pk)
    dentistas = Dentista.objects.all()
    if request.method == 'POST':
        form = UpdateCitaForm(request.POST, request.FILES)
        if form.is_valid():
            
            cita.informe = form.cleaned_data['informe']
            cita.tratamiento = form.cleaned_data['tratamiento']
            cita.atendida = True

            cita.save()
            

            return redirect('core:expediente', cita.paciente.id)
            
    else:
        form = UpdateCitaForm(instance=cita)
        
        
    return render(request, 'core/cita_update.html', {'form':form, 'dentista_list':dentistas, 'cita':cita})


        
        
class NuevoUser(LoginRequiredMixin, CreateView):
    model = User
    template_name = 'core/user_form.html'
    form_class = NuevoUserForm
    success_url = reverse_lazy('home')
    
    def get_form(self, form_class = None):
        form = super(NuevoUser, self).get_form()
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario:'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contraseña: '})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Confirmar contraseña: '})
        return form
    
    def get_initial(self):
        return {
            'is_superuser':True,
        }

class UserUpdate(SuperuserRequiredMixin, UpdateView):
    model = User
    template_name = 'core/user_update.html'
    form_class = NuevoUserForm
    success_url = reverse_lazy('login')
    
    def get_form(self, form_class = None):
        form = super(UserUpdate, self).get_form()
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario:'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contraseña: '})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Confirmar contraseña: '})
        return form