#!/bin/bash

# Leer la contraseña desde la variable de entorno
# password="$GASTOS_DB_PASSWORD"
password=$(cat config/config.json | jq -r ".password")

# Verificar si la contraseña está vacía
if [ -z "$password" ]; then
    echo "Error: La contraseña no está configurada en la variable de entorno GASTOS_DB_PASSWORD"
    exit 1
fi

# Ejecutar el script para crear el usuario y la DB
psql -U postgres -f config/setup_db.sql

# Ejecutar el script para crear la tabla de transacciones
psql -U postgres -d gastos_db -f config/crear_tabla_transacciones.sql
