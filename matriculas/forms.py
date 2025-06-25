from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import date
from .models import (
    Estudiante,
    Carrera,
    Modalidad,
    PeriodoAcademico,
    EstadoMatricula,
    Matricula,
    MetodoPago,
    Pago,
    Pais,
    DivisionPolitica,
    Ciudad,
    CampoEstudio,
)


class BaseForm(forms.ModelForm):
    """Formulario base con estilos CSS personalizados"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure_fields()
    
    def configure_fields(self):
        """Configura estilos CSS personalizados para todos los campos"""
        base_style = """
            width: 100%;
            padding: 12px 16px;
            border: 2px solid #e1e5e9;
            border-radius: 8px;
            font-size: 16px;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background-color: #ffffff;
            transition: all 0.3s ease;
            box-sizing: border-box;
        """
        
        focus_style = """
            border-color: #4f46e5;
            box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1);
            outline: none;
        """
        
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({
                    'style': base_style,
                    'placeholder': f'Ingrese {field.label.lower() if field.label else field_name}',
                    'onfocus': f"this.style.cssText='{base_style + focus_style}'",
                    'onblur': f"this.style.cssText='{base_style}'"
                })
            elif isinstance(field.widget, forms.EmailInput):
                field.widget.attrs.update({
                    'style': base_style,
                    'placeholder': 'ejemplo@correo.com',
                    'onfocus': f"this.style.cssText='{base_style + focus_style}'",
                    'onblur': f"this.style.cssText='{base_style}'"
                })
            elif isinstance(field.widget, forms.DateInput):
                field.widget.attrs.update({
                    'style': base_style,
                    'type': 'date',
                    'onfocus': f"this.style.cssText='{base_style + focus_style}'",
                    'onblur': f"this.style.cssText='{base_style}'"
                })
            elif isinstance(field.widget, forms.Textarea):
                textarea_style = base_style.replace('padding: 12px 16px;', 'padding: 12px 16px; min-height: 100px; resize: vertical;')
                field.widget.attrs.update({
                    'style': textarea_style,
                    'placeholder': f'Ingrese {field.label.lower() if field.label else field_name}',
                    'rows': 4,
                    'onfocus': f"this.style.cssText='{textarea_style + focus_style}'",
                    'onblur': f"this.style.cssText='{textarea_style}'"
                })
            elif isinstance(field.widget, forms.Select):
                select_style = base_style + 'cursor: pointer; background-image: url("data:image/svg+xml;charset=UTF-8,<svg xmlns=\'http://www.w3.org/2000/svg\' fill=\'%23666\' viewBox=\'0 0 24 24\'><path d=\'M7 10l5 5 5-5z\'/></svg>"); background-repeat: no-repeat; background-position: right 12px center; background-size: 20px; appearance: none;'
                field.widget.attrs.update({
                    'style': select_style,
                    'onfocus': f"this.style.cssText='{select_style + focus_style}'",
                    'onblur': f"this.style.cssText='{select_style}'"
                })
            elif isinstance(field.widget, forms.NumberInput):
                field.widget.attrs.update({
                    'style': base_style,
                    'min': '0',
                    'onfocus': f"this.style.cssText='{base_style + focus_style}'",
                    'onblur': f"this.style.cssText='{base_style}'"
                })
            else:
                field.widget.attrs.update({
                    'style': base_style,
                    'onfocus': f"this.style.cssText='{base_style + focus_style}'",
                    'onblur': f"this.style.cssText='{base_style}'"
                })

class EstudianteForm(BaseForm):
    """Formulario para registro/edición de estudiantes"""
    
    class Meta:
        model = Estudiante
        fields = '__all__'
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'cedula': 'Número de cédula',
            'fecha_nacimiento': 'Fecha de nacimiento',
            'genero': 'Género',
            'celular': 'Número de celular',
            'correo': 'Correo electrónico',
            'direccion': 'Dirección completa',
            'ciudad': 'Ciudad de residencia',
        }
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'genero': forms.Select(choices=[
                ('', 'Seleccione género'),
                ('Masculino', 'Masculino'),
                ('Femenino', 'Femenino'),
                ('Otro', 'Otro'),
            ]),
            'direccion': forms.Textarea(attrs={'rows': 3}),
            'correo': forms.EmailInput(),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Configurar campo ciudad con queryset vacío inicialmente
        self.fields['ciudad'].queryset = Ciudad.objects.all().order_by('nombre')
        self.fields['ciudad'].required = False
        
        # Si hay datos, cargar las ciudades correspondientes
        if 'ciudad' in self.data:
            try:
                ciudad_id = int(self.data.get('ciudad'))
                self.fields['ciudad'].queryset = Ciudad.objects.filter(id=ciudad_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.ciudad:
            self.fields['ciudad'].queryset = Ciudad.objects.filter(
                division=self.instance.ciudad.division
            )
    
    def clean_cedula(self):
        """Validar formato de cédula"""
        cedula = self.cleaned_data.get('cedula')
        if cedula:
            # Remover espacios y guiones
            cedula = cedula.replace(' ', '').replace('-', '')
            if not cedula.isdigit() or len(cedula) < 8:
                raise ValidationError('La cédula debe contener al menos 8 dígitos.')
        return cedula
    
    def clean_fecha_nacimiento(self):
        """Validar que la fecha de nacimiento sea lógica"""
        fecha = self.cleaned_data.get('fecha_nacimiento')
        if fecha:
            edad = (date.today() - fecha).days // 365
            if edad < 16 or edad > 100:
                raise ValidationError('La edad debe estar entre 16 y 100 años.')
        return fecha
    
    def clean_celular(self):
        """Validar formato de celular"""
        celular = self.cleaned_data.get('celular')
        if celular:
            celular = celular.replace(' ', '').replace('-', '').replace('(', '').replace(')', '')
            if not celular.isdigit() or len(celular) < 10:
                raise ValidationError('El número de celular debe tener al menos 10 dígitos.')
        return celular

class CarreraForm(BaseForm):
    """Formulario para carreras académicas"""
    
    class Meta:
        model = Carrera
        fields = '__all__'
        labels = {
            'nombre': 'Nombre de la carrera',
            'descripcion': 'Descripción detallada',
            'estado': 'Estado actual',
            'semestres': 'Número de semestres',
            'campo': 'Campo de estudio',
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
            'estado': forms.Select(choices=[
                ('', 'Seleccione estado'),
                ('Activo', 'Activo'),
                ('Inactivo', 'Inactivo'),
                ('En revisión', 'En revisión'),
            ]),
            'semestres': forms.NumberInput(attrs={'min': '1', 'max': '12'}),
        }
    
    def clean_semestres(self):
        """Validar número de semestres"""
        semestres = self.cleaned_data.get('semestres')
        if semestres and (semestres < 1 or semestres > 12):
            raise ValidationError('El número de semestres debe estar entre 1 y 12.')
        return semestres

class ModalidadForm(BaseForm):
    """Formulario para modalidades de estudio"""
    
    class Meta:
        model = Modalidad
        fields = '__all__'
        labels = {
            'nombre': 'Nombre de la modalidad',
           
        }
      
class PeriodoAcademicoForm(BaseForm):
    """Formulario para períodos académicos"""
    
    class Meta:
        model = PeriodoAcademico
        fields = '__all__'
        labels = {
            'nombre': 'Nombre del período',
            'fecha_inicio': 'Fecha de inicio',
            'fecha_fin': 'Fecha de finalización',
            'inicio_matricula': 'Inicio de matrículas',
            'fin_matricula': 'Fin de matrículas',
        }
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
            'inicio_matricula': forms.DateInput(attrs={'type': 'date'}),
            'fin_matricula': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def clean(self):
        """Validar coherencia de fechas"""
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')
        inicio_matricula = cleaned_data.get('inicio_matricula')
        fin_matricula = cleaned_data.get('fin_matricula')
        
        if fecha_inicio and fecha_fin:
            if fecha_inicio >= fecha_fin:
                raise ValidationError('La fecha de inicio debe ser anterior a la fecha de fin.')
        
        if inicio_matricula and fin_matricula:
            if inicio_matricula >= fin_matricula:
                raise ValidationError('El inicio de matrículas debe ser anterior al fin de matrículas.')
        
        if inicio_matricula and fecha_inicio:
            if inicio_matricula > fecha_inicio:
                raise ValidationError('Las matrículas deben comenzar antes o el mismo día que inicie el período.')
        
        return cleaned_data

class EstadoMatriculaForm(BaseForm):
    """Formulario para estados de matrícula"""
    
    class Meta:
        model = EstadoMatricula
        fields = '__all__'
        labels = {
            'descripcion': 'Estado de matrícula',
        }

class MatriculaForm(BaseForm):
    """Formulario para matrículas de estudiantes"""
    
    class Meta:
        model = Matricula
        fields = ['estudiante', 'carrera', 'modalidad', 'periodo', 'estado', 'fecha_matricula']
        labels = {
            'estudiante': 'Estudiante',
            'carrera': 'Carrera',
            'modalidad': 'Modalidad de estudio',
            'periodo': 'Período académico',
            'estado': 'Estado de la matrícula',
            'fecha_matricula': 'Fecha de matrícula',
        }
        widgets = {
            'fecha_matricula': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Filtrar solo carreras activas
        self.fields['carrera'].queryset = Carrera.objects.filter(estado='Activo')
        
        # Filtrar solo períodos actuales/futuros
        today = timezone.now().date()
        self.fields['periodo'].queryset = PeriodoAcademico.objects.filter(
            fecha_fin__gte=today
        ).order_by('fecha_inicio')
    
    def clean(self):
        """Validar que no exista matrícula duplicada"""
        cleaned_data = super().clean()
        estudiante = cleaned_data.get('estudiante')
        carrera = cleaned_data.get('carrera')
        periodo = cleaned_data.get('periodo')
        
        if estudiante and carrera and periodo:
            # Verificar si ya existe una matrícula para este estudiante, carrera y período
            existing = Matricula.objects.filter(
                estudiante=estudiante,
                carrera=carrera,
                periodo=periodo
            )
            
            if self.instance.pk:
                existing = existing.exclude(pk=self.instance.pk)
            
            if existing.exists():
                raise ValidationError(
                    'Ya existe una matrícula para este estudiante en esta carrera y período.'
                )
        
        return cleaned_data

class MetodoPagoForm(BaseForm):
    """Formulario para métodos de pago"""
    
    class Meta:
        model = MetodoPago
        fields = '__all__'
        labels = {
            'descripcion': 'Método de pago',
        }

class PagoForm(BaseForm):
    """Formulario para registro de pagos"""
    
    class Meta:
        model = Pago
        fields = '__all__'
        labels = {
            'matricula': 'Matrícula',
            'fecha_pago': 'Fecha del pago',
            'monto': 'Monto pagado',
            'metodo': 'Método de pago',
            'estado': 'Estado del pago',
        }
        widgets = {
            'fecha_pago': forms.DateInput(attrs={'type': 'date'}),
            'monto': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
            'estado': forms.Select(choices=[
                ('', 'Seleccione estado'),
                ('Pendiente', 'Pendiente'),
                ('Completado', 'Completado'),
                ('Cancelado', 'Cancelado'),
                ('Reembolsado', 'Reembolsado'),
            ]),
        }
    
    def clean_monto(self):
        """Validar que el monto sea positivo"""
        monto = self.cleaned_data.get('monto')
        if monto and monto <= 0:
            raise ValidationError('El monto debe ser mayor a cero.')
        return monto
    
    def clean_fecha_pago(self):
        """Validar que la fecha de pago no sea futura"""
        fecha = self.cleaned_data.get('fecha_pago')
        if fecha and fecha > date.today():
            raise ValidationError('La fecha de pago no puede ser futura.')
        return fecha

# ——— Formularios para ubicación geográfica ———

class PaisForm(BaseForm):
    """Formulario para países"""
    
    class Meta:
        model = Pais
        fields = '__all__'
        labels = {
            'nombre': 'Nombre del país',
        }

class DivisionPoliticaForm(BaseForm):
    """Formulario para divisiones políticas (estados, provincias, etc.)"""
    
    class Meta:
        model = DivisionPolitica
        fields = '__all__'
        labels = {
            'nombre': 'Nombre de la división',
            'pais': 'País',
        }

class CiudadForm(BaseForm):
    """Formulario para ciudades"""
    
    class Meta:
        model = Ciudad
        fields = '__all__'
        labels = {
            'nombre': 'Nombre de la ciudad',
            'division': 'División política',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Mostrar todas las divisiones por defecto
        self.fields['division'].queryset = DivisionPolitica.objects.all().order_by('nombre')

        # Si se seleccionó una división desde el formulario (por POST)
        if 'division' in self.data:
            try:
                division_id = int(self.data.get('division'))
                self.fields['division'].queryset = DivisionPolitica.objects.filter(id=division_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.division:
            # Si se está editando una ciudad existente
            self.fields['division'].queryset = DivisionPolitica.objects.filter(
                pais=self.instance.division.pais
            )


class CampoEstudioForm(BaseForm):
    """Formulario para campos de estudio"""
    
    class Meta:
        model = CampoEstudio
        fields = '__all__'
        labels = {
            'nombre': 'Nombre del campo de estudio',
        }

# ——— Formularios auxiliares para AJAX ———

class FiltroCarreraForm(forms.Form):
    """Formulario para filtrar carreras por campo de estudio"""
    campo = forms.ModelChoiceField(
        queryset=CampoEstudio.objects.all(),
        empty_label="Todos los campos",
        required=False,
        widget=forms.Select(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500'
        })
    )

class FiltroCiudadForm(forms.Form):
    """Formulario para filtrar ciudades por país y división"""
    pais = forms.ModelChoiceField(
        queryset=Pais.objects.all(),
        empty_label="Seleccione país",
        required=False,
        widget=forms.Select(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500',
            'onchange': 'loadDivisiones(this.value)'
        })
    )
    
    division = forms.ModelChoiceField(
        queryset=DivisionPolitica.objects.none(),
        empty_label="Seleccione división",
        required=False,
        widget=forms.Select(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500',
            'onchange': 'loadCiudades(this.value)'
        })
    )