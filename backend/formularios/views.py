from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Formulario, Respuesta, RespuestaPregunta
from .serializers import (
    FormularioSerializer,
    RespuestaSerializer,
    RespuestaCreateSerializer
)

# Vista para listar todos los formularios y crear uno nuevo (solo administradores)
class FormularioListCreateView(generics.ListCreateAPIView):
    queryset = Formulario.objects.all()
    serializer_class = FormularioSerializer
    permission_classes = [IsAdminUser]  # Solo administradores pueden crear formularios

    def get_queryset(self):
        """
        Filtra los formularios según el rol del usuario:
        - Administradores ven todos los formularios.
        - Coordinadores ven solo formularios asignados a ellos.
        - Gestores ven solo formularios asignados a ellos.
        """
        user = self.request.user
        if user.role == 'ADMINISTRADOR':
            return Formulario.objects.all()
        elif user.role == 'COORDINADOR':
            return Formulario.objects.filter(asignado_a_coordinadores=True)
        elif user.role == 'GESTOR':
            return Formulario.objects.filter(asignado_a_gestores=True)
        return Formulario.objects.none()

# Vista para ver, actualizar o eliminar un formulario específico (solo administradores)
class FormularioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Formulario.objects.all()
    serializer_class = FormularioSerializer
    permission_classes = [IsAdminUser]  # Solo administradores pueden editar o eliminar formularios

# Vista para listar todas las respuestas a un formulario (solo administradores y coordinadores)
class RespuestaListView(generics.ListAPIView):
    serializer_class = RespuestaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Devuelve las respuestas al formulario. 
        Los administradores ven todas las respuestas, los coordinadores solo las de sus centros.
        """
        formulario_id = self.kwargs['formulario_id']
        user = self.request.user
        if user.role == 'ADMINISTRADOR':
            return Respuesta.objects.filter(formulario_id=formulario_id)
        elif user.role == 'COORDINADOR':
            return Respuesta.objects.filter(formulario_id=formulario_id, usuario__role='GESTOR')
        return Respuesta.objects.none()

# Vista para crear una respuesta a un formulario (cualquier usuario)
class RespuestaCreateView(generics.CreateAPIView):
    serializer_class = RespuestaCreateSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        formulario_id = self.kwargs['formulario_id']
        request.data['formulario'] = formulario_id  # Asociar la respuesta al formulario
        request.data['usuario'] = request.user.id   # Asociar la respuesta al usuario actual
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Vista para obtener los detalles de una respuesta específica
class RespuestaDetailView(generics.RetrieveAPIView):
    queryset = Respuesta.objects.all()
    serializer_class = RespuestaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Devuelve la respuesta solo si el usuario es el dueño (gestor), o es administrador o coordinador.
        """
        user = self.request.user
        if user.role == 'ADMINISTRADOR':
            return Respuesta.objects.all()
        elif user.role == 'COORDINADOR':
            return Respuesta.objects.filter(usuario__role='GESTOR')
        elif user.role == 'GESTOR':
            return Respuesta.objects.filter(usuario=user)
        return Respuesta.objects.none()

