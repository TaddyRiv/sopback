from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password

from apps.empleados.serializers import EmpleadoSerializer
    
from .models import Login

from rest_framework import viewsets
from .models import Empleado
from .serializers import EmpleadoSerializer

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        "access": str(refresh.access_token),
        "refresh": str(refresh)
    }

@api_view(['POST'])
def login_usuario(request):
    email = request.data.get('email')
    password = request.data.get('password')

    try:
        user = Login.objects.get(email=email)

        if not check_password(password, user.password_hash):
            return Response({"error": "Credenciales incorrectas"}, status=400)

        tokens = get_tokens_for_user(user)

        return Response({
            "access": tokens["access"],
            "refresh": tokens["refresh"],
            "usuario": user.nombre
        })

    except Login.DoesNotExist:
        return Response({"error": "Usuario no existe"}, status=404)
    
class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all().order_by('-id')
    serializer_class = EmpleadoSerializer