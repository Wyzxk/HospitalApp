from django.db import models

# Create your models here.

class Sedes(models.Model):
    nombre_s = models.CharField(max_length=30)
    horario_s = models.CharField(max_length=30)
    ubicacion_s = models.CharField(max_length=50)
    activo_s = models.CharField(max_length=8)
    class Meta:
        db_table = "sedes"

class Doctores(models.Model):
    identificacion_d = models.CharField(max_length=30)
    nombres_d = models.CharField(max_length=50)
    apellidos_d = models.CharField(max_length=50)
    correo_d = models.EmailField()
    direccion_d = models.CharField(max_length=50)
    telefono_d = models.CharField(max_length=10)
    foto_d = models.ImageField(upload_to='doctores/',null=True)
    sede_d = models.ForeignKey(Sedes, on_delete = models.CASCADE)
    activo_d = models.CharField(max_length=8)
    class Meta:
        db_table = "doctores"

    
class Pacientes(models.Model):
    identificacion_p = models.CharField(max_length=30)
    nombres_p = models.CharField(max_length=50)
    apellidos_p = models.CharField(max_length=50)
    correo_p = models.EmailField()
    edad_p = models.IntegerField()
    direccion_p = models.CharField(max_length=50)
    telefono_p = models.CharField(max_length=10)
    foto_p = models.ImageField(upload_to='pacientes/')
    sede_p = models.ForeignKey(Sedes, on_delete = models.CASCADE)
    doctor_p = models.ForeignKey(Doctores, on_delete = models.CASCADE)
    activo_p = models.CharField(max_length=8)
    class Meta:
        db_table = "pacientes"
