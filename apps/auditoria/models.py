from django.db import models
from apps.empleados.models import Empleado, Login


class Bitacora(models.Model):
    login = models.ForeignKey(Login, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    accion = models.TextField()
    detalle = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Acción {self.id}"