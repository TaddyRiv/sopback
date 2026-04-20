from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PedidoDetalleViewSet, crear_compra, PedidoViewSet

router = DefaultRouter()
router.register(r'', PedidoViewSet)
router.register(r'detalles', PedidoDetalleViewSet)

urlpatterns = [
    path('comprar/', crear_compra),
    path('', include(router.urls)),
]