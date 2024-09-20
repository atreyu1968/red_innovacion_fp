import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';  // Importar estilos globales
import App from './App';  // Importar el componente App principal
import { BrowserRouter } from 'react-router-dom';  // Importar el enrutador

// Renderizar la aplicación dentro de un Router
ReactDOM.render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>,
  document.getElementById('root')  // Montar la aplicación en el elemento con id 'root'
);

