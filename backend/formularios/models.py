from django.db import models
from usuarios.models import Usuario

# Modelo para el Formulario
class Formulario(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    asignado_a_coordinadores = models.BooleanField(default=False)
    asignado_a_gestores = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

# Modelo para la Pregunta dentro de un Formulario
class Pregunta(models.Model):
    TIPO_PREGUNTA = [
        ('abierta', 'Abierta'),
        ('seleccion_multiple', 'Selección Múltiple'),
    ]

    texto = models.CharField(max_length=255)
    tipo = models.CharField(max_length=20, choices=TIPO_PREGUNTA)
    formulario = models.ForeignKey(Formulario, related_name='preguntas', on_delete=models.CASCADE)

    def __str__(self):
        return self.texto

# Modelo para las Opciones de una Pregunta de Selección Múltiple
class Opcion(models.Model):
    texto = models.CharField(max_length=255)
    pregunta = models.ForeignKey(Pregunta, related_name='opciones', on_delete=models.CASCADE)

    def __str__(self):
        return self.texto

# Modelo para las Respuestas de los Usuarios
class Respuesta(models.Model):
    formulario = models.ForeignKey(Formulario, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Respuesta de {self.usuario.username} al formulario {self.formulario.nombre}"

# Modelo para las Respuestas a cada Pregunta
class RespuestaPregunta(models.Model):
    respuesta = models.ForeignKey(Respuesta, related_name='respuestas_preguntas', on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    texto_respuesta = models.TextField(null=True, blank=True)  # Para respuestas abiertas
    opcion_seleccionada = models.ForeignKey(Opcion, null=True, blank=True, on_delete=models.CASCADE)  # Para respuestas de selección múltiple

    def __str__(self):
        return f"Respuesta a la pregunta {self.pregunta.texto}"

