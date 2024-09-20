
from django.urls import path
from . import views

urlpatterns = [
    # Rutas para la gestión de formularios
    path('', views.FormularioListCreateView.as_view(), name='formulario-list-create'),
    path('<int:pk>/', views.FormularioDetailView.as_view(), name='formulario-detail'),

    # Rutas para la gestión de respuestas
    path('<int:formulario_id>/responder/', views.RespuestaCreateView.as_view(), name='formulario-responder'),
    path('<int:formulario_id>/respuestas/', views.RespuestaListView.as_view(), name='formulario-respuestas'),

    # Ruta para detalles de una respuesta específica
    path('respuestas/<int:pk>/', views.RespuestaDetailView.as_view(), name='respuesta-detail'),
]
