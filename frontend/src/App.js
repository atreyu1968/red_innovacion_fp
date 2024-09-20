import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './components/Login';
import Register from './components/Register';
import AdminPanel from './components/AdminPanel';
import CoordinadorPanel from './components/CoordinadorPanel';
import GestorPanel from './components/GestorPanel';
import Formularios from './components/Formularios';
import SubirCSV from './components/SubirCSV';

const App = () => {
  return (
    <Router>
      <div>
        <Routes>
          {/* Ruta para el login */}
          <Route path="/login" element={<Login />} />

          {/* Ruta para el registro */}
          <Route path="/register" element={<Register />} />

          {/* Ruta para el panel de administrador */}
          <Route path="/admin" element={<AdminPanel />} />

          {/* Ruta para el panel de coordinador */}
          <Route path="/coordinador" element={<CoordinadorPanel />} />

          {/* Ruta para el panel de gestor */}
          <Route path="/gestor" element={<GestorPanel />} />

          {/* Ruta para ver formularios (puede ser usada por cualquier usuario autenticado) */}
          <Route path="/formularios" element={<Formularios />} />

          {/* Ruta para subir CSV (solo para administradores) */}
          <Route path="/admin/subir_csv" element={<SubirCSV />} />

          {/* Ruta por defecto (redirección o página 404) */}
          <Route path="*" element={<Login />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;

