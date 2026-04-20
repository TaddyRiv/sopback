from rest_framework import serializers
from .models import Empleado


class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

    def validate_email(self, value):
        if value and "@" not in value:
            raise serializers.ValidationError("Correo inválido")
        return value