import os
import django
import random
from datetime import date, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.catalogos.models import (
    Turno, EstadoCivil, Nacionalidad, Estado, TipoContacto, Salario
)
from apps.clientes.models import Cliente
from apps.empleados.models import Empleado
from apps.productos.models import CategoriaProducto, Producto


# =========================
# CATALOGOS
# =========================
def seed_catalogos():
    print("Catalogos...")

    Turno.objects.bulk_create([
        Turno(descripcion="Mañana"),
        Turno(descripcion="Tarde"),
        Turno(descripcion="Noche"),
    ], ignore_conflicts=True)

    EstadoCivil.objects.bulk_create([
        EstadoCivil(descripcion="Soltero"),
        EstadoCivil(descripcion="Casado"),
        EstadoCivil(descripcion="Divorciado"),
    ], ignore_conflicts=True)

    Nacionalidad.objects.bulk_create([
        Nacionalidad(descripcion="Boliviana"),
        Nacionalidad(descripcion="Peruana"),
        Nacionalidad(descripcion="Argentina"),
    ], ignore_conflicts=True)

    Estado.objects.bulk_create([
        Estado(descripcion="Activo"),
        Estado(descripcion="Inactivo"),
    ], ignore_conflicts=True)

    TipoContacto.objects.bulk_create([
        TipoContacto(descripcion="Padre"),
        TipoContacto(descripcion="Madre"),
        TipoContacto(descripcion="Hermano"),
    ], ignore_conflicts=True)

    Salario.objects.bulk_create([
        Salario(descripcion="Bajo", monto=2500),
        Salario(descripcion="Medio", monto=4000),
        Salario(descripcion="Alto", monto=6000),
    ], ignore_conflicts=True)


# =========================
# CLIENTES
# =========================
def seed_clientes():
    print("Clientes...")

    for i in range(20):
        Cliente.objects.create(
            ci_o_nit=f"CI{i}XYZ",
            nombre=f"Cliente {i}",
            fecha_nacimiento=date(1990, 1, 1) + timedelta(days=random.randint(0, 10000)),
            celular=f"700000{i}",
            email=f"cliente{i}@mail.com",
            direccion=f"Calle falsa {i}"
        )


# =========================
# PRODUCTOS
# =========================
def seed_productos():
    print("Productos...")

    categorias = []
    for nombre in ["Bebidas", "Comidas", "Postres"]:
        cat = CategoriaProducto.objects.create(
            nombre=nombre,
            descripcion=f"Categoria {nombre}"
        )
        categorias.append(cat)

    for i in range(20):
        Producto.objects.create(
            nombre=f"Producto {i}",
            descripcion=f"Descripcion del producto {i}",
            precio=random.randint(5, 50),
            disponible=True,
            categoria=random.choice(categorias)
        )


# =========================
# EMPLEADOS
# =========================
def seed_empleados():
    print("Empleados...")

    turnos = list(Turno.objects.all())
    estados_civiles = list(EstadoCivil.objects.all())
    nacionalidades = list(Nacionalidad.objects.all())
    estados = list(Estado.objects.all())
    tipos_contacto = list(TipoContacto.objects.all())
    salarios = list(Salario.objects.all())

    for i in range(10):
        Empleado.objects.create(
            nombre_empleado=f"Empleado {i}",
            ci=f"CIEMP{i}",
            tel_fijo=f"400000{i}",
            cel=f"700000{i}",
            tel_contacto=f"711111{i}",
            nombre_contacto=f"Contacto {i}",
            email=f"empleado{i}@mail.com",
            direccion=f"Direccion {i}",
            fecha_ingreso=date.today() - timedelta(days=random.randint(0, 1000)),

            turno=random.choice(turnos),
            estado_civil=random.choice(estados_civiles),
            nacionalidad=random.choice(nacionalidades),
            estado=random.choice(estados),
            tipo_contacto=random.choice(tipos_contacto),
            salario=random.choice(salarios)
        )


# =========================
# RUN
# =========================
if __name__ == "__main__":
    seed_catalogos()
    seed_clientes()
    seed_productos()
    seed_empleados()
    print("Datos completos creados correctamente")