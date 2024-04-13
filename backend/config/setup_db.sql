-- Leer la contraseña desde el archivo de configuración
\set password `cat config.json | jq -r ".password"`

-- Eliminar la base de datos si ya existe
DROP DATABASE IF EXISTS gastos_db;

-- Eliminar el usuario si ya existe
DROP USER IF EXISTS gastos_user;

-- Crear la base de datos
CREATE DATABASE gastos_db;

-- Crear el usuario y establecer la contraseña
CREATE USER gastos_user WITH PASSWORD :'password';

-- Otorgar privilegios al usuario sobre la base de datos
GRANT ALL PRIVILEGES ON DATABASE gastos_db TO gastos_user;