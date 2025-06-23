from django import forms
from .models import (
    Estudiante,
    Carrera,
    Modalidad,
    PeriodoAcademico,
    EstadoMatricula,
    Matricula,
    MetodoPago,
    Pago,
)

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'

class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = '__all__'

class ModalidadForm(forms.ModelForm):
    class Meta:
        model = Modalidad
        fields = '__all__'

class PeriodoAcademicoForm(forms.ModelForm):
    class Meta:
        model = PeriodoAcademico
        fields = '__all__'

class EstadoMatriculaForm(forms.ModelForm):
    class Meta:
        model = EstadoMatricula
        fields = '__all__'

class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = ['estudiante','carrera','modalidad','periodo','estado','fecha_matricula']

class MetodoPagoForm(forms.ModelForm):
    class Meta:
        model = MetodoPago
        fields = '__all__'

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = '__all__'


from django import forms
from .models import (
    Pais, DivisionPolitica, Ciudad,
    CampoEstudio, Carrera, Modalidad,
    Estudiante, PeriodoAcademico, EstadoMatricula,
    Matricula, MetodoPago, Pago,
)

class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = '__all__'

class DivisionPoliticaForm(forms.ModelForm):
    class Meta:
        model = DivisionPolitica
        fields = '__all__'

class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = '__all__'

class CampoEstudioForm(forms.ModelForm):
    class Meta:
        model = CampoEstudio
        fields = '__all__'

# …y deja el resto igual para Carrera, Modalidad, Estudiante, etc.…
