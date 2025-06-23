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
