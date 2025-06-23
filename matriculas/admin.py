from django.contrib import admin
from .models import (
    Pais,
    DivisionPolitica,
    Ciudad,
    CampoEstudio,
    Estudiante,
    PeriodoAcademico,
    EstadoMatricula,
    Carrera,
    Modalidad,
    Matricula,
    MetodoPago,
    Pago,
)

@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(DivisionPolitica)
class DivisionPoliticaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'pais')
    list_filter = ('pais',)
    search_fields = ('nombre',)

@admin.register(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'division')
    list_filter = ('division',)
    search_fields = ('nombre',)

@admin.register(CampoEstudio)
class CampoEstudioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'cedula', 'correo', 'ciudad')
    list_filter = ('ciudad',)
    search_fields = ('nombre','apellido','cedula')

@admin.register(PeriodoAcademico)
class PeriodoAcademicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'fecha_inicio', 'fecha_fin')
    list_filter = ('nombre',)

@admin.register(EstadoMatricula)
class EstadoMatriculaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    search_fields = ('descripcion',)

@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'campo', 'estado', 'semestres')
    list_filter = ('campo', 'estado')
    search_fields = ('nombre',)

@admin.register(Modalidad)
class ModalidadAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'estudiante', 'carrera', 'modalidad',
        'periodo', 'estado', 'fecha_matricula'
    )
    list_filter = ('periodo','estado')
    search_fields = ('estudiante__nombre','estudiante__apellido')

@admin.register(MetodoPago)
class MetodoPagoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    search_fields = ('descripcion',)

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'matricula', 'fecha_pago',
        'monto', 'metodo', 'estado'
    )
    list_filter = ('metodo',)
    search_fields = ('matricula__estudiante__nombre',)
