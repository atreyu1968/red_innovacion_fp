import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const Formularios = () => {
  const [formularios, setFormularios] = useState([]);
  const [loading, setLoading] = useState(true);

  // Función para obtener la lista de formularios desde la API
  const fetchFormularios = async () => {
    try {
      const response = await axios.get('http://localhost:8000/api/formularios/');
      setFormularios(response.data);
      setLoading(false);
    } catch (error) {
      toast.error('Error al cargar los formularios.');
      setLoading(false);
    }
  };

  // Hook useEffect para cargar los formularios cuando el componente se monta
  useEffect(() => {
    fetchFormularios();
  }, []);

  if (loading) {
    return <div>Cargando formularios...</div>;
  }

  return (
    <div>
      <h1>Formularios Disponibles</h1>
      <div className="formularios-list">
        {formularios.length === 0 ? (
          <p>No hay formularios disponibles.</p>
        ) : (
          formularios.map((formulario) => (
            <div key={formulario.id} className="formulario-item">
              <h3>{formulario.nombre}</h3>
              <p>{formulario.descripcion}</p>
              <Link to={`/formularios/${formulario.id}`}>Ver Detalles</Link>
            </div>
          ))
        )}
      </div>
      <ToastContainer />
    </div>
  );
};

export default Formularios;

