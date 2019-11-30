from django.urls import path
from .views import home, NuevaPublicacion, NuevoMedicamento, NuevoTratamiento, NuevaEspecialidad

urlpatterns = [
    path('', home, name="home"),
]

core_patterns = ([
    path('nuevapublicacion', NuevaPublicacion.as_view(), name = 'nuevapublicacion'),
    path('nuevaespecialidad', NuevaEspecialidad.as_view(), name = 'nuevaespecialidad'),
    path('nuevomedicamento', NuevoMedicamento.as_view(), name = 'nuevomedicamento'),
    path('nuevotratamiento', NuevoTratamiento.as_view(), name = 'nuevotratamiento'),
    
], 'core')