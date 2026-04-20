from rest_framework import serializers
from .models import Pedido, PedidoDetalle


class PedidoDetalleSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.CharField(source='producto.nombre')

    class Meta:
        model = PedidoDetalle
        fields = ['id', 'producto_nombre', 'cantidad', 'precio_unitario', 'subtotal']


class PedidoSerializer(serializers.ModelSerializer):
    cliente_nombre = serializers.CharField(source='cliente.nombre')
    empleado_nombre = serializers.CharField(source='empleado.nombre_empleado')
    detalles = PedidoDetalleSerializer(many=True)

    class Meta:
        model = Pedido
        fields = [
            'id',
            'cliente_nombre',
            'empleado_nombre',
            'fecha',
            'estado',
            'total',
            'detalles'
        ]

class PedidoDetalleListSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.CharField(source='producto.nombre')
    pedido_id = serializers.IntegerField(source='pedido.id')

    class Meta:
        model = PedidoDetalle
        fields = [
            'id',
            'pedido_id',
            'producto_nombre',
            'cantidad',
            'precio_unitario',
            'subtotal'
        ]