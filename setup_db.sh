#!/bin/bash

# Leer la contraseña desde la variable de entorno
password="$GASTOS_DB_PASSWORD"

# Verificar si la contraseña está vacía
if [ -z "$password" ]; then
    echo "Error: La contraseña no está configurada en la variable de entorno GASTOS_DB_PASSWORD"
    exit 1
fi

# Ejecutar el script para crear el usuario y la DB
PGPASSWORD="$password" psql -U postgres -w -f setup_db.sql

# Ejecutar el script para crear la tabla de transacciones
PGPASSWORD="$password" psql -U gastos_user -d gastos_db -w -f crear_tabla_transacciones.sql
