from django.urls import path
from .views import (
    EstudianteListView,
    EstudianteCreateView,
    MatriculaCreateView,
    PeriodoListView,
    PeriodoCreateView,
    EstadoMatriculaListView,
    EstadoMatriculaCreateView,
    CarreraListView,
    CarreraCreateView,
    ModalidadListView,
    ModalidadCreateView,
    MetodoPagoListView,
    MetodoPagoCreateView,
    PagoListView,
    PagoCreateView,
)

urlpatterns = [
    # — Estudiantes y Matrículas —
    path('', EstudianteListView.as_view(), name='estudiante_list'),
    path('estudiantes/nuevo/', EstudianteCreateView.as_view(), name='estudiante_create'),
    path('matriculas/nuevo/', MatriculaCreateView.as_view(), name='matricula_create'),

    # — Períodos Académicos —
    path('periodos/', PeriodoListView.as_view(), name='periodo_list'),
    path('periodos/nuevo/', PeriodoCreateView.as_view(), name='periodo_create'),

    # — Estados de Matrícula —
    path('estados/', EstadoMatriculaListView.as_view(), name='estado_list'),
    path('estados/nuevo/', EstadoMatriculaCreateView.as_view(), name='estado_create'),

    # — Carreras —
    path('carreras/', CarreraListView.as_view(), name='carrera_list'),
    path('carreras/nuevo/', CarreraCreateView.as_view(), name='carrera_create'),

    # — Modalidades —
    path('modalidades/', ModalidadListView.as_view(), name='modalidad_list'),
    path('modalidades/nuevo/', ModalidadCreateView.as_view(), name='modalidad_create'),

    # — Métodos de Pago —
    path('metodos_pago/', MetodoPagoListView.as_view(), name='metodopago_list'),
    path('metodos_pago/nuevo/', MetodoPagoCreateView.as_view(), name='metodopago_create'),

    # — Pagos —
    path('pagos/', PagoListView.as_view(), name='pago_list'),
    path('pagos/nuevo/', PagoCreateView.as_view(), name='pago_create'),
]
