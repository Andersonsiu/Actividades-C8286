# Instrucciones para Configurar el Entorno

Estas instrucciones te guiarán para configurar y ejecutar el sistema de recomendación en tu entorno local.

## Requisitos Previos

-   Docker
-   Docker Compose
-   Python 3.8 o superior
-   pip (gestor de paquetes de Python)
-  MongoDB

## 1. Clonar el Repositorio

Primero, clona el repositorio del proyecto desde GitHub.

`git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio` 

## 2. Configurar Variables de Entorno

Crea un archivo `.env` en el directorio raíz del proyecto y define las siguientes variables de entorno:

- MONGO_INITDB_ROOT_USERNAME=admin
- MONGO_INITDB_ROOT_PASSWORD=admin
- MONGO_INITDB_DATABASE=recomendaciones
- REDIS_HOST=redis
- REDIS_PORT=6379` 

## 3. Configurar el Entorno Python

Crea un entorno virtual y activa el entorno:

``python3 -m venv myenv
source myenv/bin/activate  # En Windows usa `myenv\Scripts\activate` `` 

Instala las dependencias del proyecto:

`pip install -r requirements.txt` 

## 4. Configurar Docker y Docker Compose

### Dockerfile

El proyecto incluye varios Dockerfiles para diferentes servicios. Asegúrate de que estén en el directorio correcto (`docker/`).

### docker-compose.yml

El archivo `docker-compose.yml` debe estar en el directorio raíz del proyecto. Asegúrate de que contenga los servicios necesarios (MongoDB, Redis, Flask, Locust, etc.).

## 5. Construir y Levantar los Contenedores

Ejecuta el siguiente comando para construir y levantar todos los contenedores definidos en `docker-compose.yml`:

`sudo docker-compose up --build` 

Este comando descargará las imágenes necesarias, construirá los contenedores y los levantará. Asegúrate de que todos los servicios estén funcionando correctamente.

## 6. Inicializar la Base de Datos

Inicializa la base de datos MongoDB con datos de ejemplo:

`sudo docker-compose run init_db` 

## 7. Ejecutar el Servidor Flask

Si el contenedor de Flask no se levanta automáticamente, puedes ejecutarlo manualmente:

`sudo docker-compose up flask_app` 

## 8. Verificar el Funcionamiento

Abre tu navegador y navega a `http://localhost:5000/test` para verificar que el servidor Flask esté funcionando correctamente.

## 9. Ejecutar Pruebas de Carga con Locust

Levanta el servicio Locust para realizar pruebas de carga:

`sudo docker-compose up locust` 

Luego, abre tu navegador y navega a `http://localhost:8089` para acceder a la interfaz de Locust y realizar pruebas de carga.

## 10. Monitoreo y Logging

Los servicios de monitoreo y logging (Prometheus, Grafana, ELK stack) se configuran y levantan automáticamente con Docker Compose. Asegúrate de que los contenedores correspondientes estén corriendo y configura los dashboards en Grafana.

### Acceder a Grafana

Abre tu navegador y navega a `http://localhost:3000` para acceder a Grafana. Usa las credenciales por defecto (usuario: `admin`, contraseña: `admin`) para iniciar sesión y configurar tus dashboards.

## Conclusión

Siguiendo estos pasos, deberías tener el entorno completo configurado y funcionando en tu máquina local. Si encuentras algún problema durante el proceso de configuración, revisa la documentación y los archivos de configuración para asegurarte de que todo esté correctamente definido.
