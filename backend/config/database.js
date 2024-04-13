// Importa Sequelize
const { Sequelize } = require('sequelize');

// Configura la conexión a la base de datos PostgreSQL
const sequelize = new Sequelize('gastos_db', 'postgres', 'kX<2jzq*%Z4Gt,A', {
  host: 'localhost',
  dialect: 'postgres'
});

// Exporta la instancia de Sequelize configurada
module.exports = sequelize;