from rest_framework import serializers
from .models import Usuario, CIFP, IES

# Serializador para el modelo de Usuario
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'role', 'is_active', 'is_staff']
        read_only_fields = ['is_active', 'is_staff']

# Serializador para el modelo CIFP
class CIFPSerializer(serializers.ModelSerializer):
    class Meta:
        model = CIFP
        fields = ['id', 'nombre_cifp', 'codigo_cifp']

# Serializador para el modelo IES
class IESSerializer(serializers.ModelSerializer):
    class Meta:
        model = IES
        fields = ['id', 'nombre_ies', 'codigo_ies']

