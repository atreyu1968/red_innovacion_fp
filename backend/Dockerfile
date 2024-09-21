# Usar una imagen oficial de Python como imagen base
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de dependencias (requirements.txt) al contenedor
COPY requirements.txt .

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación al contenedor
COPY . .

# Exponer el puerto en el que se ejecutará Django
EXPOSE 8000

# Ejecutar la aplicación con el servidor de desarrollo de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Se inicie el contenedor y se aplique la migración de la base de datos
COPY ./backend/init_setup.sh /app/init_setup.sh
RUN chmod +x /app/init_setup.sh
