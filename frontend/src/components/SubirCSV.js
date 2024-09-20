import React, { useState } from 'react';
import axios from 'axios';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const SubirCSV = () => {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  // Manejar la selección de un archivo
  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  // Manejar la subida del archivo CSV al backend
  const handleUpload = async (e) => {
    e.preventDefault();
    if (!file) {
      toast.error('Por favor selecciona un archivo CSV.');
      return;
    }

    setLoading(true);
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://localhost:8000/api/auth/subir_csv/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      // Notificación de éxito
      toast.success(response.data.message);
    } catch (error) {
      toast.error('Error al subir el archivo. Verifica el formato.');
    } finally {
      setLoading(false);
      setFile(null); // Limpiar el archivo después de subirlo
    }
  };

  return (
    <div>
      <h1>Subir CSV</h1>
      <form onSubmit={handleUpload}>
        <div>
          <input type="file" accept=".csv" onChange={handleFileChange} />
        </div>
        <button type="submit" disabled={loading}>
          {loading ? 'Subiendo...' : 'Subir CSV'}
        </button>
      </form>
      <ToastContainer />
    </div>
  );
};

export default SubirCSV;

