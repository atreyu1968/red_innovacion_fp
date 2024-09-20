import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const Register = () => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [role, setRole] = useState('GESTOR'); // Por defecto, un nuevo usuario podría ser 'GESTOR'
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  // Función para manejar el registro de un nuevo usuario
  const handleRegister = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await axios.post('http://localhost:8000/api/auth/register/', {
        username,
        email,
        password,
        role,
      });

      // Notificación de éxito
      toast.success('Registro exitoso. Ahora puedes iniciar sesión.');

      // Redirigir al usuario a la página de inicio de sesión
      setTimeout(() => {
        navigate('/login');
      }, 1000);
    } catch (error) {
      toast.error('Error en el registro. Verifica los datos ingresados.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>Registrarse</h1>
      <form onSubmit={handleRegister}>
        <div>
          <label>Nombre de usuario:</label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Email:</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Contraseña:</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Rol:</label>
          <select value={role} onChange={(e) => setRole(e.target.value)} required>
            <option value="GESTOR">Gestor</option>
            <option value="COORDINADOR">Coordinador</option>
            <option value="ADMINISTRADOR">Administrador</option>
          </select>
        </div>
        <button type="submit" disabled={loading}>
          {loading ? 'Registrando...' : 'Registrarse'}
        </button>
      </form>
      <ToastContainer />
    </div>
  );
};

export default Register;

