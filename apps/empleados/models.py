from django.db import models
from apps.catalogos.models import (
    Turno,
    EstadoCivil,
    Nacionalidad,
    Estado,
    TipoContacto,
    Salario
)


class Empleado(models.Model):
    nombre_empleado = models.CharField(max_length=200)
    ci = models.CharField(max_length=20, unique=True, null=True, blank=True)
    tel_fijo = models.CharField(max_length=20, blank=True, null=True)
    cel = models.CharField(max_length=20, blank=True, null=True)

    tel_contacto = models.CharField(max_length=20, blank=True, null=True)
    nombre_contacto = models.CharField(max_length=200, blank=True, null=True)

    email = models.EmailField(blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    fecha_ingreso = models.DateField()

    turno = models.ForeignKey(Turno, on_delete=models.RESTRICT)
    estado_civil = models.ForeignKey(EstadoCivil, on_delete=models.RESTRICT)
    nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.RESTRICT)
    estado = models.ForeignKey(Estado, on_delete=models.RESTRICT)
    tipo_contacto = models.ForeignKey(TipoContacto, on_delete=models.RESTRICT)
    salario = models.ForeignKey(Salario, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nombre_empleado


class Login(models.Model):
    empleado = models.OneToOneField(
        Empleado,
        on_delete=models.CASCADE,
        related_name="login"
    )
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    password_hash = models.CharField(max_length=255)
    estado = models.CharField(max_length=20)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_login = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nombre