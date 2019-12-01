from django.urls import path
from .views import home, NuevaPublicacion, NuevoMedicamento, NuevoTratamiento, NuevaEspecialidad, NuevaPromocion, Blog
from .views import TratamientoList, MedicamentoList, TratamientoUpdate, MedicamentoUpdate,EspecialidadUpdate, EspecialidadList, TratamientoDelete, MedicamentoDelete,EspecialidadDelete

urlpatterns = [
    path('', home, name="home"),
]

core_patterns = ([
    path('nuevapublicacion', NuevaPublicacion.as_view(), name = 'nuevapublicacion'),
    path('nuevaespecialidad', NuevaEspecialidad.as_view(), name = 'nuevaespecialidad'),
    path('nuevomedicamento', NuevoMedicamento.as_view(), name = 'nuevomedicamento'),
    path('nuevotratamiento', NuevoTratamiento, name = 'nuevotratamiento'),
    path('nuevapromocion', NuevaPromocion, name = 'nuevapromocion'),
    path('blog', Blog, name = 'blog'),
    path('tratamientos', TratamientoList.as_view(), name = 'tratamientos'),
    path('medicamentos', MedicamentoList.as_view(), name = 'medicamentos'),
    path('especialidad', EspecialidadList.as_view(), name = 'especialidades'),
    path('actualizartratamientos/<int:pk>', TratamientoUpdate.as_view(), name = 'tratamientoupdate'),
    path('actualizarmedicamentos/<int:pk>', MedicamentoUpdate.as_view(), name = 'updatemedicamento'),
    path('actualizarespecialidad/<int:pk>', EspecialidadUpdate.as_view(), name = 'updateespecialidad'),
    path('eliminartratamientos/<int:pk>', TratamientoDelete.as_view(), name = 'tratamientodelete'),
    path('eliminarmedicamentos/<int:pk>', MedicamentoDelete.as_view(), name = 'medicamentodelete'),
    path('eliminarespecialidad/<int:pk>', EspecialidadDelete.as_view(), name = 'especialidaddelete'),
    
], 'core')