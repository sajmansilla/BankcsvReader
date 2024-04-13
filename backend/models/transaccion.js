// Importa Sequelize y la configuración de la conexión a la base de datos
const { Sequelize, DataTypes } = require('sequelize');
const sequelize = require('../config/database');

// Define el modelo de datos para las transacciones
const Transaccion = sequelize.define('transacciones', {
  // Define los campos de la tabla de transacciones
  id: {
    type: DataTypes.BIGINT,
    allowNull: false,
    primaryKey: true
  },
  booking_date: {
    type: DataTypes.DATE
  },
  value_date: {
    type: DataTypes.DATE
  },
  transaction_payment_details: {
    type: DataTypes.STRING,
    allowNull: false
  },
  debit: {
    type: DataTypes.DECIMAL(10,2),
    allowNull: false
  },
  credit: {
    type: DataTypes.DECIMAL(10, 2),
    allowNull: false
  },
  currency: {
    type: DataTypes.STRING,
    allowNull: false
  },
  description_text: {
    type: DataTypes.STRING,
    allowNull: false
  }
}, {
  // Configuración adicional del modelo
  timestamps: false // Desactiva la inclusión de subqueries
});

// Exporta el modelo de datos de las transacciones
module.exports = Transaccion;