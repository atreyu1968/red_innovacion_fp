import React, { useState } from 'react';
import axios from 'axios';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const ActualizarApp = () => {
  const [loading, setLoading] = useState(false);

  const handleActualizar = async () => {
    setLoading(true);
    try {
      const response = await axios.post('http://localhost:8000/api/auth/actualizar_aplicacion/');
      toast.success(response.data.message);
      console.log(response.data);
    } catch (error) {
      if (error.response && error.response.data.message) {
        toast.error(error.response.data.message);
      } else {
        toast.error('Error al intentar actualizar la aplicación.');
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2>Actualizar Aplicación</h2>
      <p>Haga clic en el botón para obtener las últimas actualizaciones del sistema y reiniciar la aplicación.</p>
      <button onClick={handleActualizar} disabled={loading}>
        {loading ? 'Actualizando...' : 'Actualizar Aplicación'}
      </button>
      <ToastContainer />
    </div>
  );
};

export default ActualizarApp;

