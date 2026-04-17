from django.contrib import admin
from .models import Pedido, PedidoDetalle, NotaVenta

admin.site.register(Pedido)
admin.site.register(PedidoDetalle)
admin.site.register(NotaVenta)