from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import (
    Estudiante,
    PeriodoAcademico,
    EstadoMatricula,
    Carrera,
    Modalidad,
    Matricula,
    MetodoPago,
    Pago,
)
from .forms import (
    EstudianteForm,
    MatriculaForm,
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
