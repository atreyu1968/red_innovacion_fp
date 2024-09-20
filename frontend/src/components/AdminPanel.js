import React from 'react';
import { Link } from 'react-router-dom';
import ActualizarApp from './ActualizarApp';

const AdminPanel = () => {
  return (
    <div>
      <h1>Panel de Administración</h1>
      <div className="admin-panel">
        <div className="admin-panel-section">
          <h2>Gestión de Formularios</h2>
          <Link to="/admin/formularios">Ver Formularios</Link>
          <Link to="/admin/crear_formulario">Crear Nuevo Formulario</Link>
        </div>

        <div className="admin-panel-section">
          <h2>Gestión de Usuarios</h2>
          <Link to="/admin/usuarios">Ver Usuarios</Link>
          <Link to="/admin/subir_csv">Subir Usuarios desde CSV</Link>
        </div>

        <div className="admin-panel-section">
          <h2>Actualizar Aplicación</h2>
          <ActualizarApp />
        </div>
      </div>
    </div>
  );
};

export default AdminPanel;

