#!/bin/bash

# Leer la contraseña desde el archivo de configuración
password=$(cat config.json | jq -r ".password")

# Validar si la tabla ya existe
exists_table=$(psql -U gastos_user -d gastos_db -tAc "SELECT CASE WHEN EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema = 'public' AND table_name = 'transacciones') THEN 'true' ELSE 'false' END")

# Eliminar la tabla si ya existe
if [ "$exists_table" = "true" ]; then
    psql -U gastos_user -d gastos_db -c "DROP TABLE transacciones"
fi

# Crear la tabla transacciones
psql -U gastos_user:$password -d gastos_db -f crear_tabla_transacciones.sql
