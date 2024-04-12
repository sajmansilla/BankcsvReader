-- Si la tabla ya existe, eliminarla
DROP TABLE IF EXISTS transacciones;

-- Crear la tabla transacciones
CREATE TABLE transacciones (
    id SERIAL PRIMARY KEY,
    concepto VARCHAR(255) NOT NULL,
    cantidad DECIMAL(10, 2) NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
