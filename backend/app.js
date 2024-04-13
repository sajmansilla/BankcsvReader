//TODO: Poner TODO LO DE LA BD EN VARIABLES
// Importa Express
const express = require('express');
// Importa el modelo de transacciones
const Transaccion = require('./models/transaccion');

// Crea una instancia de Express
const app = express();

// Configura el puerto en el que escuchará el servidor
const PORT = process.env.PORT || 3000;

// Ruta para obtener todas las transacciones
app.get('/transacciones', async (req, res) => {
  try {
    // Utiliza Sequelize para recuperar todas las transacciones de la base de datos
    const transacciones = await Transaccion.findAll();

    // Devuelve las transacciones como respuesta en formato JSON
    res.json(transacciones);
  } catch (error) {
    // Si hay algún error al recuperar las transacciones, devuelve un mensaje de error
    console.error('Error al recuperar las transacciones:', error);
    res.status(500).json({ error: 'Error al recuperar las transacciones' });
  }
});

// Inicia el servidor
app.listen(PORT, () => {
  console.log(`Servidor escuchando en el puerto ${PORT}`);
});
