-- Crear la base de datos
CREATE DATABASE red_innovacion_fp;

-- Conectar a la base de datos creada
\c red_innovacion_fp;

-- Crear tabla de usuarios
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    rol VARCHAR(50) NOT NULL CHECK (rol IN ('ADMINISTRADOR', 'COORDINADOR', 'GESTOR')),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Crear tabla de formularios
CREATE TABLE formularios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    asignado_a_coordinadores BOOLEAN DEFAULT FALSE,
    asignado_a_gestores BOOLEAN DEFAULT FALSE,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Crear tabla de preguntas dentro de los formularios
CREATE TABLE preguntas (
    id SERIAL PRIMARY KEY,
    texto VARCHAR(255) NOT NULL,
    tipo VARCHAR(50) NOT NULL CHECK (tipo IN ('abierta', 'seleccion_multiple')),
    formulario_id INTEGER REFERENCES formularios(id) ON DELETE CASCADE
);

-- Crear tabla de opciones para preguntas de selección múltiple
CREATE TABLE opciones (
    id SERIAL PRIMARY KEY,
    texto VARCHAR(255) NOT NULL,
    pregunta_id INTEGER REFERENCES preguntas(id) ON DELETE CASCADE
);

-- Crear tabla de respuestas de los usuarios a los formularios
CREATE TABLE respuestas (
    id SERIAL PRIMARY KEY,
    formulario_id INTEGER REFERENCES formularios(id) ON DELETE CASCADE,
    usuario_id INTEGER REFERENCES usuarios(id) ON DELETE CASCADE,
    fecha_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Crear tabla de respuestas individuales a cada pregunta dentro del formulario
CREATE TABLE respuestas_preguntas (
    id SERIAL PRIMARY KEY,
    respuesta_id INTEGER REFERENCES respuestas(id) ON DELETE CASCADE,
    pregunta_id INTEGER REFERENCES preguntas(id) ON DELETE CASCADE,
    texto_respuesta TEXT,
    opcion_seleccionada_id INTEGER REFERENCES opciones(id) ON DELETE SET NULL
);

-- Crear índices para mejorar el rendimiento de las consultas
CREATE INDEX idx_usuario_email ON usuarios(email);
CREATE INDEX idx_formulario_fecha_creacion ON formularios(fecha_creacion);
CREATE INDEX idx_respuesta_usuario ON respuestas(usuario_id);

-- Datos de ejemplo (opcional)
INSERT INTO usuarios (nombre, email, rol) VALUES ('Admin Central', 'admin@fp.com', 'ADMINISTRADOR');
INSERT INTO formularios (nombre, descripcion, asignado_a_coordinadores, asignado_a_gestores) 
VALUES ('Formulario de ejemplo', 'Descripción del formulario de ejemplo', TRUE, FALSE);

