from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Ruta para el panel de administración
    path('admin/', admin.site.urls),

    # Rutas para la aplicación de usuarios
    path('api/auth/', include('usuarios.urls')),

    # Rutas para la aplicación de formularios
    path('api/formularios/', include('formularios.urls')),
]

# Sirviendo archivos estáticos y media en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

