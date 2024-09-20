
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Usuario

@receiver(post_save, sender=Usuario)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    """
    Señal para crear un perfil de usuario automáticamente cuando se crea un nuevo usuario.
    """
    if created:
        # Aquí puedes agregar lógica personalizada, como crear un perfil o enviar un email
        print(f"Usuario {instance.username} creado con éxito.")
