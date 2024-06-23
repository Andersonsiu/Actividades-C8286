# Instrucciones para Configurar el Entorno

## Requisitos

Antes de comenzar, asegúrese de tener instalados los siguientes componentes en su sistema:

1. **Docker**: Para ejecutar MongoDB en un contenedor.
2. **Python 3.10**: Lenguaje de programación utilizado en el proyecto.
3. **Pip**: Administrador de paquetes para Python.

## Pasos para Configurar el Entorno

Configuración de MongoDB


a. Iniciar el Contenedor de MongoDB
Si no tienes el contenedor de MongoDB, puedes crearlo usando Docker:

docker pull mongo:4.4
docker run -d -p 27017:27017 --name my-mongo mongo:4.4

Para iniciar el contenedor en el futuro:
docker start my-mongo


b. Verificar la Configuración en MongoDB Compass

Puedes verificar la estructura de la base de datos usando MongoDB Compass. Abre MongoDB Compass y conecta a localhost:27017 para ver las colecciones y datos insertados.


