# Instrucciones para Configurar el Entorno

## Requisitos

Antes de comenzar, asegúrese de tener instalados los siguientes componentes en su sistema:

1. **Docker**: Para ejecutar MongoDB en un contenedor.
2. **Python 3.10**: Lenguaje de programación utilizado en el proyecto.
3. **Pip**: Administrador de paquetes para Python.

## Pasos para Configurar el Entorno


### 1. Configuración de MongoDB

#### a. Iniciar el Contenedor de MongoDB


Si no tienes el contenedor de MongoDB, puedes crearlo usando Docker:

- `docker pull mongo:4.4`
- `docker run -d -p 27017:27017 --name my-mongo mongo:4.4` 


Para iniciar el contenedor en el futuro:

`docker start my-mongo` 


#### b. Verificar la Configuración en MongoDB Compass

Puedes verificar la estructura de la base de datos usando MongoDB Compass. Abre MongoDB Compass y conecta a `localhost:27017` para ver las colecciones y datos insertados.


### 2. Población de la Base de Datos

Ejecuta el script para poblar la base de datos con datos de ejemplo:

`python3 src/poblacion_datos.py` 


### 3. Ejecutar el Motor de Recomendación

Ejecuta los scripts del motor de recomendación para generar y evaluar las recomendaciones:


- `python3 src/filtrado_colaborativo.py`
- `python3 src/clustering.py` 

### 4. Ejecutar Jupyter Notebooks

Para visualizar los resultados y gráficos, abre los notebooks de Jupyter:

`jupyter notebook` 

Abre los notebooks en el navegador y ejecuta las celdas para ver los análisis y visualizaciones.

## Solución de Problemas

-   **Contenedor de Docker no Inicia**: Verifica si el puerto 27017 está libre o intenta reiniciar Docker.
-   **Errores de Conexión a MongoDB**: Asegúrate de que el contenedor de MongoDB está en ejecución y que estás utilizando la URL correcta (`mongodb://localhost:27017/`).
