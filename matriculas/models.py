from django.db import models

# ——— Localización geográfica ———
class Pais(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class DivisionPolitica(models.Model):
    nombre = models.CharField(max_length=100)
    pais   = models.ForeignKey(Pais, on_delete=models.PROTECT, related_name='divisiones')
    def __str__(self):
        return f"{self.nombre} ({self.pais})"

class Ciudad(models.Model):
    nombre    = models.CharField(max_length=100)
    division  = models.ForeignKey(DivisionPolitica, on_delete=models.PROTECT, related_name='ciudades')
    def __str__(self):
        return f"{self.nombre}, {self.division}"

# ——— Campo de estudio ———
class CampoEstudio(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

# ——— Carrera y Modalidad ———
class Carrera(models.Model):
    nombre      = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    estado      = models.CharField(max_length=50)          # p.ej. Activo / Inactivo
    semestres   = models.PositiveIntegerField()
    campo       = models.ForeignKey(CampoEstudio, on_delete=models.PROTECT, related_name='carreras')
    def __str__(self):
        return self.nombre

class Modalidad(models.Model):
    nombre      = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)
    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    nombre           = models.CharField(max_length=100)
    apellido         = models.CharField(max_length=100)
    cedula           = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    genero           = models.CharField(max_length=10)
    celular          = models.CharField(max_length=20)
    correo           = models.EmailField()
    direccion        = models.TextField()
    ciudad           = models.ForeignKey(
                          Ciudad,
                          on_delete=models.PROTECT,
                          related_name='estudiantes',
                          null=True,    # permite valores nulos
                          blank=True    # permite dejarlo vacío en formularios
                      )

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class PeriodoAcademico(models.Model):
    nombre           = models.CharField(max_length=50)
    fecha_inicio     = models.DateField()
    fecha_fin        = models.DateField()
    inicio_matricula = models.DateField()
    fin_matricula    = models.DateField()
    def __str__(self):
        return self.nombre

class EstadoMatricula(models.Model):
    descripcion = models.CharField(max_length=50)
    def __str__(self):
        return self.descripcion

class Matricula(models.Model):
    estudiante  = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='matriculas')
    carrera     = models.ForeignKey(Carrera, on_delete=models.PROTECT)
    modalidad   = models.ForeignKey(Modalidad, on_delete=models.PROTECT)
    periodo     = models.ForeignKey(PeriodoAcademico, on_delete=models.PROTECT)
    estado      = models.ForeignKey(EstadoMatricula, on_delete=models.PROTECT)
    fecha_matricula = models.DateField()
    def __str__(self):
        return f"{self.estudiante} → {self.carrera} ({self.modalidad})"

# ——— Pago ———
class MetodoPago(models.Model):
    descripcion = models.CharField(max_length=50)
    def __str__(self):
        return self.descripcion

class Pago(models.Model):
    matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE, related_name='pagos')
    fecha_pago = models.DateField()
    monto      = models.DecimalField(max_digits=10, decimal_places=2)
    metodo     = models.ForeignKey(MetodoPago, on_delete=models.PROTECT)
    estado     = models.CharField(max_length=20)
    def __str__(self):
        return f"Pago {self.id} – {self.matricula.estudiante}"
