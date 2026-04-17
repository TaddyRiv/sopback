from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/ventas/', include('apps.ventas.urls')),
    path('api/clientes/', include('apps.clientes.urls')),
    path('api/productos/', include('apps.productos.urls')),
    path('api/empleados/', include('apps.empleados.urls')),
    path('api/ventas/', include('apps.ventas.urls')),
]
