from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from braces.views import SuperuserRequiredMixin, LoginRequiredMixin
from django.utils.decorators import method_decorator
from .models import Publicacion, Especialidad, Tratamiento, Medicamento
from .forms import NuevaPublicacionForm, NuevoMedicamentoForm, NuevaEspecialidadForm, NuevoTratamientoForm

def home(request):
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
    