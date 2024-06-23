# Diseño y Arquitectura del Sistema de Recomendación

## Introducción

Este documento describe el diseño y la arquitectura del sistema de recomendación desarrollado en el proyecto. El sistema utiliza una base de datos NoSQL (MongoDB) y técnicas de filtrado colaborativo y clustering para ofrecer recomendaciones personalizadas a los usuarios.

## Estructura de la Base de Datos

La base de datos MongoDB está diseñada con las siguientes colecciones:

- **usuarios**: Almacena la información de los usuarios.
- **productos**: Almacena la información de los productos.
- **interacciones**: Almacena las interacciones entre usuarios y productos.
- **recomendaciones_usuario**: Almacena las recomendaciones generadas para cada usuario.

## Arquitectura del Sistema
La arquitectura del sistema está compuesta por los siguientes módulos:

- Ingesta de Datos: Scripts para poblar la base de datos con datos de usuarios, productos e interacciones.
- Motor de Recomendación: Implementación de los algoritmos de filtrado colaborativo y clustering.
- Evaluación: Módulos para evaluar la precisión y efectividad de las recomendaciones.
- Interfaz de Usuario: Dashboards y visualizaciones para mostrar los resultados y análisis de las recomendaciones.
  
## Flujo de Trabajo

- Ingesta de Datos: Los datos de usuarios, productos e interacciones se ingestan en MongoDB.
- Generación de Recomendaciones: Se ejecutan los algoritmos de recomendación para generar recomendaciones personalizadas.
- Almacenamiento de Resultados: Las recomendaciones generadas se almacenan en la colección recomendaciones_usuario.
- Evaluación: Se evalúa la efectividad de las recomendaciones utilizando las métricas mencionadas.
- Visualización: Se generan gráficos y dashboards para visualizar los resultados y análisis.
