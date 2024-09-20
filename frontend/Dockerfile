# 1. Usar una imagen base de Node.js para compilar la aplicación React
FROM node:16-alpine AS build

# 2. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar los archivos de dependencias (package.json y package-lock.json) al contenedor
COPY package*.json ./

# 4. Instalar las dependencias del proyecto
RUN npm install

# 5. Copiar el resto del código fuente al contenedor
COPY . .

# 6. Ejecutar la compilación de la aplicación para producción
RUN npm run build

# 7. Usar una imagen ligera de Nginx para servir los archivos estáticos
FROM nginx:alpine

# 8. Copiar los archivos compilados desde la fase de compilación a la carpeta predeterminada de Nginx
COPY --from=build /app/build /usr/share/nginx/html

# 9. Exponer el puerto 80 para servir la aplicación en este puerto
EXPOSE 80

# 10. Comando por defecto para iniciar Nginx
CMD ["nginx", "-g", "daemon off;"]

