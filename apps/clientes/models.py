from django.db import models


class Cliente(models.Model):
    ci_o_nit = models.CharField(max_length=20, blank=True, null=True)
    nombre = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    celular = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre