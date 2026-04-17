from django.db import transaction
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from apps.ventas.models import Pedido, PedidoDetalle, NotaVenta
from apps.productos.models import Producto
from apps.clientes.models import Cliente
from apps.empleados.models import Empleado

from rest_framework import viewsets
from .serializers import PedidoSerializer

class PedidoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Pedido.objects.all().order_by('-id')
    serializer_class = PedidoSerializer

@csrf_exempt
def crear_compra(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            cliente = Cliente.objects.get(id=data["cliente_id"])
            empleado = Empleado.objects.get(id=data["empleado_id"])
            productos = data["productos"]

            with transaction.atomic():

                # 1. Crear pedido
                pedido = Pedido.objects.create(
                    cliente=cliente,
                    empleado=empleado,
                    estado="COMPLETADO",
                    total=0
                )

                total = 0

                # 2. Crear detalles
                for item in productos:
                    producto = Producto.objects.get(id=item["producto_id"])
                    cantidad = item["cantidad"]

                    subtotal = producto.precio * cantidad
                    total += subtotal

                    PedidoDetalle.objects.create(
                        pedido=pedido,
                        producto=producto,
                        cantidad=cantidad,
                        precio_unitario=producto.precio,
                        subtotal=subtotal
                    )

                # 3. Actualizar total
                pedido.total = total
                pedido.save()

                # 4. Crear nota de venta
                NotaVenta.objects.create(
                    pedido=pedido,
                    cliente=cliente,
                    empleado=empleado,
                    total=total
                )

            return JsonResponse({
                "mensaje": "Compra realizada correctamente",
                "pedido_id": pedido.id,
                "total": total
            })

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
        
