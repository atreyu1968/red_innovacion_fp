
from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    """
    Permite el acceso solo a los administradores.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'ADMINISTRADOR'

class IsCoordinador(BasePermission):
    """
    Permite el acceso solo a los coordinadores de red.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'COORDINADOR'

class IsGestor(BasePermission):
    """
    Permite el acceso solo a los gestores de red.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'GESTOR'
