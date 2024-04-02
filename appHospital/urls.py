from django.urls import path
from .views import index, formSede,listadoSedeA, listadoSedeI,listadoInactivar,listadoActivar,editSede
from .views import formDoctores,editDoctores,listadoDoctoresA,listadoDoctoresI,listDocInactivar,listDocActivar
from .views import formPacientes,editPacientes,listadoPacientesA,listadoPacientesI,listPacActivar,listPacInactivar

urlpatterns = [
    path('', index),
    # Sedes
    path('formulariosede', formSede),
    path('editarsede/<int:id>', editSede),
    path('listadosedeA', listadoSedeA),
    path('listadosedeI', listadoSedeI),
    path('listadosedeInactivar/<int:id>', listadoInactivar),
    path('listadosedeActivar/<int:id>', listadoActivar),
    # Doctores
    path('formulariodoctores', formDoctores),
    path('editardoctor/<int:id>', editDoctores),
    path('listadodoctoresA', listadoDoctoresA),
    path('listadodoctoresI', listadoDoctoresI),
    path('listadodoctoresInactivar/<int:id>', listDocInactivar),
    path('listadodoctoresActivar/<int:id>', listDocActivar),
    # Pacientes
    path('formulariopacientes', formPacientes),
    path('editarpaciente/<int:id>', editPacientes),
    path('listadopacientesA', listadoPacientesA),
    path('listadopacientesI', listadoPacientesI),
    path('listadopacientesInactivar/<int:id>', listPacInactivar),
    path('listadopacientesActivar/<int:id>', listPacActivar),
]
