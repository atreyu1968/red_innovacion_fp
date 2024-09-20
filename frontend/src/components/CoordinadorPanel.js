import React from 'react';
import { Link } from 'react-router-dom';

const CoordinadorPanel = () => {
  return (
    <div>
      <h1>Panel de Coordinador de Red</h1>
      <div className="coordinador-panel">
        
        <div className="coordinador-panel-section">
          <h2>Gestión de Formularios</h2>
          <Link to="/coordinador/formularios">Ver Formularios Asignados</Link>
        </div>

        <div className="coordinador-panel-section">
          <h2>Respuestas de Gestores</h2>
          <Link to="/coordinador/respuestas">Ver Respuestas de los Gestores</Link>
        </div>

        <div className="coordinador-panel-section">
          <h2>Informes</h2>
          <Link to="/coordinador/informes">Generar Informes</Link>
        </div>
        
      </div>
    </div>
  );
};

export default CoordinadorPanel;

