"""
WSGI config for el proyecto de Red de Innovación de FP de Canarias.

Este archivo expone la aplicación WSGI como una variable llamada `application`.

Para más información sobre este archivo, consulta:
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Establecer la configuración predeterminada para el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Definir la aplicación WSGI
application = get_wsgi_application()

