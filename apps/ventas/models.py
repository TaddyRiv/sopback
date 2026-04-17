from django.db import models
from apps.clientes.models import Cliente
from apps.empleados.models import Empleado
from apps.productos.models import Producto


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.RESTRICT)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=30)
    total = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Pedido {self.id}"


class PedidoDetalle(models.Model):
    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
        related_name="detalles"
    )
    producto = models.ForeignKey(Producto, on_delete=models.RESTRICT)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=12, decimal_places=2)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Detalle {self.id}"


class NotaVenta(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    empleado = models.ForeignKey(Empleado, on_delete=models.RESTRICT)
    fecha = models.DateField(auto_now_add=True)
    nit = models.CharField(max_length=20, blank=True, null=True)
    razon_social = models.CharField(max_length=300, blank=True, null=True)
    total = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Nota {self.id}"