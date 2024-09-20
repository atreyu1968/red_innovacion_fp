
# Red de Innovación de FP de Canarias

Este es un sistema web para gestionar la red de innovación de Formación Profesional en Canarias. Permite a los administradores, coordinadores y gestores interactuar con formularios, respuestas y generar informes a partir de las respuestas recibidas.

## Características
- **Autenticación por roles**: Administrador, Coordinador y Gestor.
- **Creación y gestión de formularios**: Los administradores pueden crear formularios que serán respondidos por coordinadores y gestores.
- **Gestión de respuestas**: Los coordinadores y gestores pueden ver y responder a los formularios.
- **Generación de informes**: A partir de las respuestas a los formularios.
- **Carga masiva de datos**: Subida de usuarios mediante archivos CSV.

## Requisitos

Para ejecutar esta aplicación, necesitas tener instalado:
- **Docker** y **Docker Compose**
- **Node.js** (si deseas desarrollar sin Docker)
- **Python 3.x** y **Django** (si deseas desarrollar sin Docker)
- **PostgreSQL** para la base de datos

## Instalación y configuración

### Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/red-innovacion-fp-canarias.git
cd red-innovacion-fp-canarias
```

### Configuración del archivo `.env`

Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:

```bash
# Configuración de PostgreSQL
POSTGRES_DB=red_innovacion_fp
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin123
POSTGRES_HOST=db
POSTGRES_PORT=5432

# Configuración del backend Django
DJANGO_SECRET_KEY=your-secret-key-here
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

# URL de la base de datos para Django
DATABASE_URL=postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}

# Configuración del frontend React
REACT_APP_API_URL=http://localhost:8000/api

# Configuración del entorno
ENVIRONMENT=development
```

### Uso con Docker

Esta aplicación está diseñada para ejecutarse fácilmente utilizando Docker y Docker Compose. Para iniciar todos los servicios, ejecuta los siguientes comandos:

```bash
# Construir y levantar los contenedores
docker-compose up --build
```

Este comando creará y ejecutará tres contenedores:
- **Base de datos PostgreSQL**
- **Backend Django**
- **Frontend React**

### Migraciones de base de datos

Una vez que los contenedores estén levantados, abre otra terminal y ejecuta las migraciones de Django para configurar la base de datos:

```bash
docker exec -it django-app python manage.py migrate
```

### Crear un superusuario para acceder al admin de Django

Para crear un superusuario (administrador) que pueda acceder al panel de administración de Django:

```bash
docker exec -it django-app python manage.py createsuperuser
```

### Acceder a la aplicación

Una vez que todo esté en funcionamiento:

- El **frontend** estará disponible en: `http://localhost:3000`
- El **backend** (API de Django) estará disponible en: `http://localhost:8000`
- El **panel de administración de Django** estará disponible en: `http://localhost:8000/admin`

### Subir datos mediante CSV

Para subir usuarios desde un archivo CSV, accede al panel de administración y usa la interfaz disponible para cargar archivos CSV.

### Compilar el frontend para producción

Si necesitas compilar el frontend React para producción, ejecuta el siguiente comando:

```bash
docker exec -it react-app npm run build
```

Esto generará los archivos optimizados para servirlos en un servidor como Nginx.

## Desarrollo local sin Docker

Si prefieres trabajar sin Docker, sigue estos pasos para configurar el proyecto manualmente.

### Backend (Django)

1. Instalar dependencias:

   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. Configurar las variables de entorno en un archivo `.env`.

3. Ejecutar migraciones:

   ```bash
   python manage.py migrate
   ```

4. Crear un superusuario:

   ```bash
   python manage.py createsuperuser
   ```

5. Ejecutar el servidor de desarrollo:

   ```bash
   python manage.py runserver
   ```

### Frontend (React)

1. Instalar dependencias:

   ```bash
   cd frontend
   npm install
   ```

2. Ejecutar el servidor de desarrollo:

   ```bash
   npm start
   ```

El frontend estará disponible en `http://localhost:3000`.

## Estructura del proyecto

```bash
red-innovacion-fp-canarias/
│
├── backend/                   # Aplicación Django
│   ├── manage.py              # Comando principal de Django
│   ├── config/                # Configuración principal de Django
│   ├── usuarios/              # Aplicación de usuarios en Django
│   ├── formularios/           # Aplicación de formularios en Django
│   └── ...                    # Otros archivos de Django
│
├── frontend/                  # Aplicación React
│   ├── public/                # Archivos públicos del frontend
│   ├── src/                   # Código fuente de la aplicación React
│   └── ...                    # Otros archivos del frontend
│
├── postgres/                  # Scripts de inicialización de la base de datos
│   └── init.sql               # Script SQL para la configuración inicial
│
├── docker-compose.yml          # Configuración de Docker Compose
├── .env                        # Archivo de configuración de variables de entorno
└── README.md                   # Documentación del proyecto
```

## Tecnologías utilizadas

- **Backend**: Django, Django REST Framework
- **Frontend**: React.js
- **Base de datos**: PostgreSQL
- **Contenedores**: Docker y Docker Compose
- **Servidor web**: Nginx (opcional para producción)

## Contribuir

1. Haz un fork del proyecto.
2. Crea una nueva rama para tu funcionalidad (`git checkout -b feature/nueva-funcionalidad`).
3. Haz commit de tus cambios (`git commit -m 'Añadir nueva funcionalidad'`).
4. Empuja tu rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está licenciado bajo los términos de la [MIT License](https://opensource.org/licenses/MIT).


