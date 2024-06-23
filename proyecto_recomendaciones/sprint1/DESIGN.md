# Diseño y Arquitectura del Sistema de Recomendación

## Introducción

Este documento detalla el diseño y la arquitectura del sistema de recomendación desarrollado en el Proyecto 5. El objetivo del sistema es ofrecer recomendaciones personalizadas a los usuarios utilizando una base de datos NoSQL (MongoDB) y técnicas avanzadas de filtrado colaborativo y clustering.

## Objetivos del Diseño

- **Escalabilidad**: La arquitectura debe soportar un crecimiento en el número de usuarios y productos sin afectar el rendimiento.
- **Flexibilidad**: La estructura de la base de datos debe permitir la fácil adición de nuevos tipos de datos y relaciones.
- **Eficiencia**: Optimizar las consultas y el procesamiento de datos para proporcionar recomendaciones en tiempo real.

## Estructura de la Base de Datos

### Colecciones

El sistema utiliza cuatro colecciones principales en MongoDB:

1. **Usuarios (`usuarios`)**:
   - **Campos**:
     - `user_id`: Identificador único del usuario.
     - `nombre`: Nombre del usuario.
     - `email`: Correo electrónico del usuario.
   - **Índices**:
     - Índice en `user_id` para búsquedas rápidas.

2. **Productos (`productos`)**:
   - **Campos**:
     - `producto_id`: Identificador único del producto.
     - `nombre`: Nombre del producto.
     - `categoría`: Categoría a la que pertenece el producto.
   - **Índices**:
     - Índice en `producto_id` para búsquedas rápidas.

3. **Interacciones (`interacciones`)**:
   - **Campos**:
     - `user_id`: Identificador del usuario que realizó la interacción.
     - `producto_id`: Identificador del producto con el que se interactuó.
     - `tipo_interaccion`: Tipo de interacción (`compra`, `click`, `view`).
     - `timestamp`: Fecha y hora de la interacción.
   - **Índices**:
     - Índice compuesto en `user_id` y `producto_id` para optimizar las consultas por usuario y producto.

4. **Recomendaciones de Usuario (`recomendaciones_usuario`)**:
   - **Campos**:
     - `user_id`: Identificador del usuario.
     - `recomendaciones_usuario`: Lista de productos recomendados basados en el filtrado colaborativo de usuarios.
     - `recomendaciones_items`: Lista de productos recomendados basados en el filtrado colaborativo de ítems.
     - `recomendaciones_cluster`: Lista de productos recomendados basados en clustering.
   - **Índices**:
     - Índice en `user_id` para búsquedas rápidas.

### Esquema de la Base de Datos

![Esquema de la Base de Datos](../images/database_schema.png)

## Arquitectura del Sistema

### Componentes Principales

1. **Motor de Recomendación**:
   - **Filtrado Colaborativo**:
     - Basado en Usuarios: Recomienda productos a un usuario basándose en la similitud con otros usuarios.
     - Basado en Ítems: Recomienda productos similares a los que el usuario ya ha consumido.
   - **Clustering**:
     - Agrupa usuarios o productos en clusters basados en sus características o comportamientos para generar recomendaciones más precisas.

2. **Base de Datos MongoDB**:
   - Almacena los datos de usuarios, productos, interacciones y recomendaciones generadas.
   - Optimizada con índices para mejorar el rendimiento de las consultas.

3. **Scripts y Notebooks**:
   - **Población de la Base de Datos (`populate_db.py`)**: Inserta datos de ejemplo en MongoDB.
   - **Filtrado Colaborativo (`filtrado_colaborativo.py`)**: Implementa y evalúa el sistema de recomendación basado en usuarios e ítems.
   - **Clustering (`clustering.py`)**: Implementa y evalúa el sistema de recomendación basado en clustering.
   - **Notebooks de Jupyter**: Proporcionan una interfaz interactiva para visualizar los resultados y gráficos generados.

### Diagrama de Flujo

![Diagrama de Flujo del Sistema](../images/system_flowchart.png)

## Optimización y Escalabilidad

- **Índices en MongoDB**: Se han definido índices en los campos de búsqueda frecuente para mejorar el rendimiento de las consultas.
- **Procesamiento en Paralelo**: Uso de técnicas de multiprocessing y threading en Python para acelerar el procesamiento de datos y la generación de recomendaciones.
- **Pruebas de Carga**: Se realizarán pruebas de carga para evaluar la escalabilidad del sistema y ajustar la configuración según sea necesario.

## Conclusión

El diseño y la arquitectura del sistema de recomendación están orientados a proporcionar recomendaciones personalizadas de manera eficiente y escalable. La combinación de técnicas de filtrado colaborativo y clustering, junto con una base de datos NoSQL optimizada, garantiza un alto rendimiento y flexibilidad para adaptarse a diferentes tipos de datos y escenarios de uso.


