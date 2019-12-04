from django.urls import path
from .views import home, NuevaPublicacion, NuevoMedicamento, NuevoTratamiento, NuevaEspecialidad, NuevaPromocion, Blog
from .views import TratamientoList, MedicamentoList, TratamientoUpdate, MedicamentoUpdate,EspecialidadUpdate, EspecialidadList, TratamientoDelete, MedicamentoDelete,EspecialidadDelete
from .views import NuevoUsuario, NuevoDentista, UpdateUsuario, UpdateDentista, ModificarPublicacion , EliminarPublicacion,  ModificarPromocion, EliminarPromocion
from .views import NuevoPaciente, PacienteDelete, PacienteList, DentistaDelete, DentistaList, NuevaCategoria, CategoriaDelete, CategoriaList, CategoriaUpdate
from .views import ReestablecerPrecio, HabilitarCitas, PacienteList2, CitaList, ReservarCita, CitaList2, Expediente, CitaDelete, PacienteUpdate
from .views import PacienteList3, CitaList4, NuevaReceta, RecetaList, RecetaDelete, CitaUpdate, CitaList3

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
    path('nuevousuario/', NuevoUsuario.as_view(), name='nuevousuariod'),
    path('nuevodentista/<int:usuario>', NuevoDentista, name='nuevodentista'),
    path('updateusuario/<int:pk>', UpdateUsuario.as_view(), name='updateusuariod'),
    path('updatedentista/<int:pk>', UpdateDentista.as_view(), name='updatedentista'),
    path('modificarpromocion/<int:pk>', ModificarPromocion.as_view(), name = 'modificarpromocion'),
    path('modificarpublicacion/<int:pk>', ModificarPublicacion.as_view(), name = 'modificarpublicacion'),
    path('eliminarpromocion/<int:pk>', EliminarPromocion.as_view(), name = 'eliminarpromocion'),
    path('eliminarpublicacion/<int:pk>', EliminarPublicacion.as_view(), name = 'eliminarpublicacion'),
    path('nuevopaciente/', NuevoPaciente, name='nuevopaciente'),
    path('actualizarpacientes/<int:pk>', PacienteUpdate.as_view(), name = 'updatepaciente'),
    path('dentistas', DentistaList.as_view(), name = 'dentistas'),
    path('pacientes', PacienteList.as_view(), name = 'pacientes'),
    path('pacientes2', PacienteList2.as_view(), name = 'pacientes2'),
    path('pacientes3', PacienteList3.as_view(), name = 'pacientes3'),
    path('eliminardentista/<int:pk>', DentistaDelete.as_view(), name = 'dentistadelete'),
    path('eliminarpaciente/<int:pk>', PacienteDelete.as_view(), name = 'pacientedelete'),
    path('nuevacategoria', NuevaCategoria.as_view(), name = 'nuevacategoria'),
    path('categorias', CategoriaList.as_view(), name = 'categorias'),
    path('actualizarcategoria/<int:pk>', CategoriaUpdate.as_view(), name = 'updatecategoria'),
    path('eliminarcateogira/<int:pk>', CategoriaDelete.as_view(), name = 'categoriadelete'),
    path('reestablecerprecio/<int:pk>', ReestablecerPrecio, name = 'reestablecerprecio'),
    path('habilitarcitas', HabilitarCitas, name = 'habilitarcitas'),
    path('citas/<int:paciente>', CitaList, name = 'citas'),
    path('reservarcita/<int:paciente>/<int:pk>', ReservarCita, name = 'reservarcita'),
    path('citas2', CitaList2, name = 'citas2'),
    path('citas4', CitaList4, name = 'citas4'),
    path('eliminarcita/<int:pk>', CitaDelete.as_view(), name = 'citadelete'),
    path('expediente/<int:pk>', Expediente, name = 'expediente'),
    path('nuevareceta/<int:paciente>/', NuevaReceta.as_view(), name='nuevareceta'),
    path('recetas/<int:paciente>/', RecetaList.as_view(), name = 'recetas'),
    path('eliminarreceta/<int:pk>', RecetaDelete.as_view(), name = 'recetadelete'),
    path('updatecita/<int:pk>', CitaUpdate.as_view(), name = 'updatecita'),
    path('citas3/<int:paciente>', CitaList3.as_view(), name = 'citas3'),
    
    
    
], 'core')