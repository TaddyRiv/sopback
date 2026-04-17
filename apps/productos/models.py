from django.db import models


class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    categoria = models.ForeignKey(
        CategoriaProducto,
        on_delete=models.RESTRICT,
        related_name="productos"
    )
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre