from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from braces.views import SuperuserRequiredMixin, LoginRequiredMixin
from django.utils.decorators import method_decorator
from .models import Publicacion, Especialidad, Tratamiento, Medicamento, Promocion
from .forms import NuevaPublicacionForm, NuevoMedicamentoForm, NuevaEspecialidadForm, NuevoTratamientoForm, NuevaPromocionForm

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
    
def NuevoTratamiento(request):
    if request.method == 'POST':
        form = NuevoTratamientoForm(request.POST)
        if form.is_valid():
            form.save()
            
            ultimo = Tratamiento.objects.latest('id')
            
            instancia = Tratamiento()
            
            instancia.CalcularPN(0, ultimo.precio, ultimo.id)   
            
            return redirect('home')
    else:
        form = NuevoTratamientoForm()
    
    return render(request, 'core/tratamiento_form.html', {'form':form})

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

class MedicamentoList(ListView):
    model = Medicamento
    template_name = 'core/medicamento_list.html'

class EspecialidadList(ListView):
    model = Especialidad
    template_name = 'core/especialidad_list.html'

class TratamientoUpdate(LoginRequiredMixin, UpdateView):
    model = Tratamiento
    template_name = 'core/tratamiento_update.html'
    form_class = NuevoTratamientoForm
    success_url = reverse_lazy('core:tratamientos')

class MedicamentoUpdate(LoginRequiredMixin, UpdateView):
    model = Medicamento
    template_name = 'core/medicamento_update.html'
    form_class = NuevoMedicamentoForm
    success_url = reverse_lazy('core:medicamentos')

class EspecialidadUpdate(LoginRequiredMixin, UpdateView):
    model = Especialidad
    template_name = 'core/especialidad_update.html'
    form_class = NuevaEspecialidadForm
    success_url = reverse_lazy('core:especialidades')

class TratamientoDelete(LoginRequiredMixin, DeleteView):
    model = Tratamiento
    template_name= "core/tratamiento_delete.html"
    success_url = reverse_lazy('core:tratamientos')


class MedicamentoDelete(LoginRequiredMixin, DeleteView):
    model = Medicamento
    template_name= "core/medicamento_delete.html"
    success_url = reverse_lazy('core:medicamentos')

class EspecialidadDelete(LoginRequiredMixin, DeleteView):
    model = Especialidad
    template_name= "core/especualidad_delete.html"
    success_url = reverse_lazy('core:especialidades')



    