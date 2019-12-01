from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from braces.views import SuperuserRequiredMixin, LoginRequiredMixin
from django.utils.decorators import method_decorator
from .models import Publicacion, Especialidad, Tratamiento, Medicamento
from .forms import NuevaPublicacionForm, NuevoMedicamentoForm, NuevaEspecialidadForm, NuevoTratamientoForm

def home(request):
    publicaciones = Publicacion.objects.filter().order_by('-id')[:5]
    cantidad = Publicacion.objects.filter().count()
    ps = []
    i=0
    for p in publicaciones:
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
        return render(request, "core/home.html", {'p0':p0, 'cantidad':cantidad})
    elif cantidad == 2:
        return render(request, "core/home.html", {'p0':p0, 'p1':p1, 'cantidad':cantidad})
    elif cantidad == 3:
        return render(request, "core/home.html", {'p0':p0, 'p1':p1, 'p2':p2, 'cantidad':cantidad})
    elif cantidad == 4:
        return render(request, "core/home.html", {'p0':p0, 'p1':p1, 'p2':p2, 'p3':p3, 'cantidad':cantidad})
    elif cantidad == 5:
        return render(request, "core/home.html", {'p0':p0, 'p1':p1, 'p2':p2, 'p3':p3, 'p4':p4, 'cantidad':cantidad})
    else:
        return render(request, "core/home.html")
    

class NuevaPublicacion(SuperuserRequiredMixin, CreateView):
    model = Publicacion
    form_class = NuevaPublicacionForm
    success_url = reverse_lazy('home')
    
class NuevaEspecialidad(SuperuserRequiredMixin, CreateView):
    model = Especialidad
    form_class = NuevaEspecialidadForm
    success_url = reverse_lazy('home')

class NuevoMedicamento(SuperuserRequiredMixin, CreateView):
    model = Medicamento
    form_class = NuevoMedicamentoForm
    success_url = reverse_lazy('home')

class NuevoTratamiento(SuperuserRequiredMixin, CreateView):
    model = Tratamiento
    form_class = NuevoTratamientoForm
    success_url = reverse_lazy('home')
    