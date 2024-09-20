from rest_framework import serializers
from .models import Formulario, Pregunta, Opcion, Respuesta, RespuestaPregunta

# Serializador para el modelo Opcion
class OpcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opcion
        fields = ['id', 'texto']

# Serializador para el modelo Pregunta
class PreguntaSerializer(serializers.ModelSerializer):
    opciones = OpcionSerializer(many=True, read_only=True)  # Si es de selección múltiple, tendrá opciones

    class Meta:
        model = Pregunta
        fields = ['id', 'texto', 'tipo', 'opciones']

# Serializador para el modelo Formulario
class FormularioSerializer(serializers.ModelSerializer):
    preguntas = PreguntaSerializer(many=True, read_only=True)

    class Meta:
        model = Formulario
        fields = ['id', 'nombre', 'descripcion', 'fecha_creacion', 'asignado_a_coordinadores', 'asignado_a_gestores', 'preguntas']

# Serializador para el modelo RespuestaPregunta
class RespuestaPreguntaSerializer(serializers.ModelSerializer):
    pregunta = PreguntaSerializer(read_only=True)
    opcion_seleccionada = OpcionSerializer(read_only=True)

    class Meta:
        model = RespuestaPregunta
        fields = ['pregunta', 'texto_respuesta', 'opcion_seleccionada']

# Serializador para el modelo Respuesta
class RespuestaSerializer(serializers.ModelSerializer):
    respuestas_preguntas = RespuestaPreguntaSerializer(many=True, read_only=True)
    usuario = serializers.StringRelatedField()  # Muestra el nombre del usuario en lugar de solo el ID
    formulario = FormularioSerializer(read_only=True)

    class Meta:
        model = Respuesta
        fields = ['id', 'formulario', 'usuario', 'fecha_envio', 'respuestas_preguntas']

# Serializador para crear o actualizar RespuestaPregunta (cuando el usuario responde a una pregunta)
class RespuestaPreguntaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespuestaPregunta
        fields = ['pregunta', 'texto_respuesta', 'opcion_seleccionada']

# Serializador para crear o actualizar una Respuesta completa (con todas las respuestas a las preguntas)
class RespuestaCreateSerializer(serializers.ModelSerializer):
    respuestas_preguntas = RespuestaPreguntaCreateSerializer(many=True)

    class Meta:
        model = Respuesta
        fields = ['formulario', 'respuestas_preguntas']

    def create(self, validated_data):
        respuestas_preguntas_data = validated_data.pop('respuestas_preguntas')
        respuesta = Respuesta.objects.create(**validated_data)
        for respuesta_pregunta_data in respuestas_preguntas_data:
            RespuestaPregunta.objects.create(respuesta=respuesta, **respuesta_pregunta_data)
        return respuesta

