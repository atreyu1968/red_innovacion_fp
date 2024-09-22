# Usar una imagen oficial de Python como imagen base
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de dependencias (requirements.txt) al contenedor
COPY ./requirements.txt .

# Instalar las dependencias de Python (incluyendo psycopg2-binary en lugar de psycopg2)
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación al contenedor
COPY . .

# Copiar el script de inicialización y otorgarle permisos de ejecución
COPY ./backend/init_setup.sh /app/init_setup.sh
RUN chmod +x /app/init_setup.sh

# Exponer el puerto en el que se ejecutará Django
EXPOSE 8000

# Ejecutar el script de inicialización y luego iniciar Django
CMD ["/app/init_setup.sh"]
