from django.db import models


class Turno(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion


class EstadoCivil(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion


class Nacionalidad(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion


class Estado(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion


class TipoContacto(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion


class Salario(models.Model):
    descripcion = models.CharField(max_length=150)
    monto = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.descripcion} - {self.monto}"