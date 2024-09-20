from django.contrib import admin
from .models import Usuario, CIFP, IES

# Registro del modelo de Usuario para que sea visible en el admin de Django
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_active', 'is_staff')
    list_filter = ('role', 'is_active', 'is_staff')
    search_fields = ('username', 'email')
    ordering = ('username',)

# Registro del modelo CIFP para su gestión en el admin
@admin.register(CIFP)
class CIFPAdmin(admin.ModelAdmin):
    list_display = ('nombre_cifp', 'codigo_cifp')
    search_fields = ('nombre_cifp', 'codigo_cifp')

# Registro del modelo IES para su gestión en el admin
@admin.register(IES)
class IESAdmin(admin.ModelAdmin):
    list_display = ('nombre_ies', 'codigo_ies')
    search_fields = ('nombre_ies', 'codigo_ies')

