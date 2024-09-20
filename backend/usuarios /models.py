from django.contrib.auth.models import AbstractUser
from django.db import models

# Modelo de Usuario, basado en el sistema de autenticación de Django
class Usuario(AbstractUser):
    ADMINISTRADOR = 'ADMINISTRADOR'
    COORDINADOR = 'COORDINADOR'
    GESTOR = 'GESTOR'

    ROLE_CHOICES = [
        (ADMINISTRADOR, 'Administrador'),
        (COORDINADOR, 'Coordinador de Red'),
        (GESTOR, 'Gestor de Red'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=GESTOR)

    def __str__(self):
        return self.username


# Modelo CIFP (Centro Integrado de Formación Profesional)
class CIFP(models.Model):
    nombre_cifp = models.CharField(max_length=255)
    codigo_cifp = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre_cifp


# Modelo IES (Instituto de Educación Secundaria)
class IES(models.Model):
    nombre_ies = models.CharField(max_length=255)
    codigo_ies = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre_ies

