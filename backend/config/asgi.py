"""
ASGI config for el proyecto de Red de Innovación de FP de Canarias.

Este archivo expone la aplicación ASGI como una variable llamada `application`.

Para más información sobre este archivo, consulta:
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

# Establecer la configuración predeterminada para el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Definir la aplicación ASGI
application = get_asgi_application()

