#!/bin/bash

# Esperar a que MongoDB esté listo
while ! nc -z localhost 27017; do
  echo "Esperando a que MongoDB esté listo..."
  sleep 1
done

# Ejecutar los scripts de inicialización
python3 /docker-entrypoint-initdb.d/bd.py
python3 /docker-entrypoint-initdb.d/poblacion_datos.py
python3 /docker-entrypoint-initdb.d/datos_sinteticos.py
python3 /docker-entrypoint-initdb.d/integracion.py


