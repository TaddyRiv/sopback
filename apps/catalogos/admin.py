from django.contrib import admin
from .models import (
    Turno,
    EstadoCivil,
    Nacionalidad,
    Estado,
    TipoContacto,
    Salario
)

admin.site.register(Turno)
admin.site.register(EstadoCivil)
admin.site.register(Nacionalidad)
admin.site.register(Estado)
admin.site.register(TipoContacto)
admin.site.register(Salario)