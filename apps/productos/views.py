from rest_framework import viewsets
from .models import Producto, CategoriaProducto
from .serializers import ProductoSerializer, CategoriaSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all().order_by('-id')
    serializer_class = ProductoSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = CategoriaProducto.objects.all().order_by('-id')
    serializer_class = CategoriaSerializer