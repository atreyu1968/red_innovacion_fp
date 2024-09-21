#!/bin/bash

# Esperar a que la base de datos esté lista
echo "Esperando a que la base de datos se inicie..."
until python manage.py migrate --noinput; do
  >&2 echo "Postgres no está disponible - reintentando..."
  sleep 2
done

# Aplicar migraciones
echo "Aplicando migraciones..."
python manage.py migrate --noinput

# Crear superusuario si no existe
echo "Creando usuario administrador..."
python manage.py shell -c "
from django.contrib.auth import get_user_model;
User = get_user_model();
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
"

# Ejecutar el servidor
exec "$@"
