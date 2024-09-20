# 1. Usar una imagen base de Node.js
FROM node:16-alpine AS build

# 2. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar los archivos package.json y package-lock.json (si existe)
COPY package*.json ./

# 4. Instalar las dependencias de la aplicación
RUN npm install

# 5. Copiar todo el código de la aplicación al contenedor
COPY . .

# 6. Compilar la aplicación para producción
RUN npm run build

# 7. Servir la aplicación usando una imagen de nginx
FROM nginx:alpine

# 8. Copiar los archivos compilados de React al directorio nginx
COPY --from=build /app/build /usr/share/nginx/html

# 9. Exponer el puerto 80
EXPOSE 80

# 10. Comando por defecto para iniciar nginx
CMD ["nginx", "-g", "daemon off;"]

