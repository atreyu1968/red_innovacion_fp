from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    RegisterView, 
    UserListView, 
    SubirUsuariosCSVView, 
    SubirCIFPCSVView, 
    SubirIESCSVView,
    ActualizarAplicacionView
)

urlpatterns = [
    # Autenticación y tokens JWT
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),

    # Gestión de usuarios
    path('usuarios/', UserListView.as_view(), name='user-list'),

    # Subida de archivos CSV
    path('subir_usuarios_csv/', SubirUsuariosCSVView.as_view(), name='subir_usuarios_csv'),
    path('subir_cifp_csv/', SubirCIFPCSVView.as_view(), name='subir_cifp_csv'),
    path('subir_ies_csv/', SubirIESCSVView.as_view(), name='subir_ies_csv'),

    # Actualización de la aplicación
    path('actualizar_aplicacion/', ActualizarAplicacionView.as_view(), name='actualizar_aplicacion'),
]

