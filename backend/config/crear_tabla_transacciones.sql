-- Si la tabla ya existe, eliminarla
DROP TABLE IF EXISTS transacciones;

-- Crear la tabla transacciones
CREATE TABLE transacciones (
    id SERIAL PRIMARY KEY,
    booking_date TIMESTAMP,
    value_date TIMESTAMP,
    transaction_payment_details VARCHAR NOT NULL,
    debit DECIMAL(10, 2) NOT NULL,
    credit DECIMAL(10, 2) NOT NULL,
    currency VARCHAR(5) NOT NULL,
    description_text VARCHAR NOT NULL,
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
