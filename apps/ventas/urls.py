from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import crear_compra, PedidoViewSet

router = DefaultRouter()
router.register(r'', PedidoViewSet)

urlpatterns = [
    path('comprar/', crear_compra),
    path('', include(router.urls)),
]