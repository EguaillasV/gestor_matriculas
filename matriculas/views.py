from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import (
    CampoEstudio,
    Ciudad,
    DivisionPolitica,
    Estudiante,
    Pais,
    PeriodoAcademico,
    EstadoMatricula,
    Carrera,
    Modalidad,
    Matricula,
    MetodoPago,
    Pago,
)
from .forms import (
    CampoEstudioForm,
    CiudadForm,
    DivisionPoliticaForm,
    EstudianteForm,
    MatriculaForm,
    PaisForm,
    PeriodoAcademicoForm,
    EstadoMatriculaForm,
    CarreraForm,
    ModalidadForm,
    MetodoPagoForm,
    PagoForm,
)

# ——— Estudiantes ———
class EstudianteListView(ListView):
    model = Estudiante
    template_name = "matriculas/estudiante_list.html"

class EstudianteCreateView(CreateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = "matriculas/estudiante_form.html"
    success_url = reverse_lazy('estudiante_list')


# ——— Períodos Académicos ———
class PeriodoListView(ListView):
    model = PeriodoAcademico
    template_name = "matriculas/periodoacademico_list.html"

class PeriodoCreateView(CreateView):
    model = PeriodoAcademico
    form_class = PeriodoAcademicoForm
    template_name = "matriculas/periodoacademico_form.html"
    success_url = reverse_lazy('periodo_list')


# ——— Estados de Matrícula ———
class EstadoMatriculaListView(ListView):
    model = EstadoMatricula
    template_name = "matriculas/estadomatricula_list.html"

class EstadoMatriculaCreateView(CreateView):
    model = EstadoMatricula
    form_class = EstadoMatriculaForm
    template_name = "matriculas/estadomatricula_form.html"
    success_url = reverse_lazy('estado_list')


# ——— Carreras ———
class CarreraListView(ListView):
    model = Carrera
    template_name = "matriculas/carrera_list.html"

class CarreraCreateView(CreateView):
    model = Carrera
    form_class = CarreraForm
    template_name = "matriculas/carrera_form.html"
    success_url = reverse_lazy('carrera_list')


# ——— Modalidades ———
class ModalidadListView(ListView):
    model = Modalidad
    template_name = "matriculas/modalidad_list.html"

class ModalidadCreateView(CreateView):
    model = Modalidad
    form_class = ModalidadForm
    template_name = "matriculas/modalidad_form.html"
    success_url = reverse_lazy('modalidad_list')


# ——— Matrículas ———
class MatriculaCreateView(CreateView):
    model = Matricula
    form_class = MatriculaForm
    template_name = "matriculas/matricula_form.html"
    success_url = reverse_lazy('matricula_create')

class MatriculaListView(ListView):
    model = Matricula
    template_name = "matriculas/matricula_list.html"
    context_object_name = 'matriculas'
    paginate_by = 20  # Opcional: para paginación
    
    def get_queryset(self):
        # Optimizar consultas con select_related para evitar N+1 queries
        return Matricula.objects.select_related(
            'estudiante', 'carrera', 'periodo'
        ).order_by('-fecha_matricula')

# ——— Métodos de Pago ———
class MetodoPagoListView(ListView):
    model = MetodoPago
    template_name = "matriculas/metodopago_list.html"

class MetodoPagoCreateView(CreateView):
    model = MetodoPago
    form_class = MetodoPagoForm
    template_name = "matriculas/metodopago_form.html"
    success_url = reverse_lazy('metodopago_list')


# ——— Pagos ———
class PagoListView(ListView):
    model = Pago
    template_name = "matriculas/pago_list.html"

class PagoCreateView(CreateView):
    model = Pago
    form_class = PagoForm
    template_name = "matriculas/pago_form.html"
    success_url = reverse_lazy('pago_list')

class PaisListView(ListView):
    model = Pais
    template_name = "matriculas/pais_list.html"

class PaisCreateView(CreateView):
    model = Pais
    form_class = PaisForm
    template_name = "matriculas/pais_form.html"
    success_url = reverse_lazy('pais_list')

# ——— Divisiones Políticas ———
class DivisionPoliticaListView(ListView):
    model = DivisionPolitica
    template_name = "matriculas/divisionpolitica_list.html"

class DivisionPoliticaCreateView(CreateView):
    model = DivisionPolitica
    form_class = DivisionPoliticaForm
    template_name = "matriculas/divisionpolitica_form.html"
    success_url = reverse_lazy('division_list')

# ——— Ciudades ———
class CiudadListView(ListView):
    model = Ciudad
    template_name = "matriculas/ciudad_list.html"

class CiudadCreateView(CreateView):
    model = Ciudad
    form_class = CiudadForm
    template_name = "matriculas/ciudad_form.html"
    success_url = reverse_lazy('ciudad_list')

# ——— Campos de Estudio ———
class CampoEstudioListView(ListView):
    model = CampoEstudio
    template_name = "matriculas/campoestudio_list.html"

class CampoEstudioCreateView(CreateView):
    model = CampoEstudio
    form_class = CampoEstudioForm
    template_name = "matriculas/campoestudio_form.html"
    success_url = reverse_lazy('campo_list')