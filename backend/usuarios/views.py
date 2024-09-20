from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, AllowAny
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CIFP, IES, Usuario
from .serializers import UsuarioSerializer, CIFPSerializer, IESSerializer
import csv
from django.core.files.storage import default_storage

# Vista para el registro de usuarios
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        role = request.data.get('role')

        if Usuario.objects.filter(username=username).exists():
            return Response({'error': 'El nombre de usuario ya está en uso.'}, status=status.HTTP_400_BAD_REQUEST)

        if Usuario.objects.filter(email=email).exists():
            return Response({'error': 'El correo electrónico ya está en uso.'}, status=status.HTTP_400_BAD_REQUEST)

        user = Usuario.objects.create_user(username=username, email=email, password=password, role=role)
        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)

# Vista para obtener la lista de usuarios (solo accesible para administradores)
class UserListView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        users = Usuario.objects.all()
        serializer = UsuarioSerializer(users, many=True)
        return Response(serializer.data)

# Vista para subir CSV de usuarios
class SubirUsuariosCSVView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        file = request.FILES['file']
        file_path = default_storage.save(file.name, file)

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                username = row.get('username')
                email = row.get('email')
                role = row.get('role')

                if not Usuario.objects.filter(username=username).exists():
                    user = Usuario.objects.create_user(username=username, email=email, password="defaultpassword", role=role)
                    user.save()

        return Response({'status': 'Archivo CSV de usuarios procesado correctamente.'})

# Vista para subir CSV de CIFP
class SubirCIFPCSVView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        file = request.FILES['file']
        file_path = default_storage.save(file.name, file)

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                nombre_cifp = row.get('nombre_cifp')
                codigo_cifp = row.get('codigo_cifp')

                if not CIFP.objects.filter(codigo_cifp=codigo_cifp).exists():
                    cifp = CIFP(nombre_cifp=nombre_cifp, codigo_cifp=codigo_cifp)
                    cifp.save()

        return Response({'status': 'Archivo CSV de CIFP procesado correctamente.'})

# Vista para subir CSV de IES
class SubirIESCSVView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        file = request.FILES['file']
        file_path = default_storage.save(file.name, file)

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                nombre_ies = row.get('nombre_ies')
                codigo_ies = row.get('codigo_ies')

                if not IES.objects.filter(codigo_ies=codigo_ies).exists():
                    ies = IES(nombre_ies=nombre_ies, codigo_ies=codigo_ies)
                    ies.save()

        return Response({'status': 'Archivo CSV de IES procesado correctamente.'})

