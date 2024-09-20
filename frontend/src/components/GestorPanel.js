import React from 'react';
import { Link } from 'react-router-dom';

const GestorPanel = () => {
  return (
    <div>
      <h1>Panel de Gestor de Red</h1>
      <div className="gestor-panel">
        
        <div className="gestor-panel-section">
          <h2>Formularios Asignados</h2>
          <Link to="/gestor/formularios">Ver Formularios Asignados</Link>
        </div>

        <div className="gestor-panel-section">
          <h2>Mis Respuestas</h2>
          <Link to="/gestor/respuestas">Ver Mis Respuestas</Link>
        </div>
      </div>
    </div>
  );
};

export default GestorPanel;

