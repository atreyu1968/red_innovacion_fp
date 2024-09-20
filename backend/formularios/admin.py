from django.contrib import admin
from .models import Formulario, Pregunta, Respuesta

# Registro del modelo de Formulario en el panel de administración
@admin.register(Formulario)
class FormularioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_creacion', 'asignado_a_coordinadores', 'asignado_a_gestores')
    search_fields = ('nombre',)
    list_filter = ('asignado_a_coordinadores', 'asignado_a_gestores')
    ordering = ('fecha_creacion',)

# Registro del modelo de Pregunta en el panel de administración
@admin.register(Pregunta)
class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('texto', 'formulario', 'tipo')
    search_fields = ('texto',)
    list_filter = ('tipo', 'formulario')

# Registro del modelo de Respuesta en el panel de administración
@admin.register(Respuesta)
class RespuestaAdmin(admin.ModelAdmin):
    list_display = ('formulario', 'usuario', 'fecha_envio')
    list_filter = ('formulario', 'usuario')
    search_fields = ('usuario__username', 'formulario__nombre')
    ordering = ('fecha_envio',)

