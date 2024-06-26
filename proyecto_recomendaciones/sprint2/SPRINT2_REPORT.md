### Sprint 2: Implementación de Algoritmos de Recomendación y Evaluación

#### 1. Introducción

**Objetivos del Sprint:** El objetivo principal del Sprint 2 fue implementar y evaluar algoritmos de recomendación utilizando filtrado colaborativo y técnicas de clustering. Estos objetivos se alinean con el objetivo general del proyecto de crear un sistema de recomendación eficiente y escalable.

#### 2. Planificación

**Tareas planificadas:**

-   Implementar Filtrado Colaborativo Basado en Usuarios
-   Implementar Filtrado Colaborativo Basado en Ítems
-   Implementar Clustering de Usuarios utilizando K-means
-   Integrar los algoritmos con MongoDB
-   Generar y utilizar datos sintéticos
-   Evaluar los algoritmos implementados

#### 3. Implementación

**Descripción del trabajo realizado:** Se implementaron y evaluaron diversos algoritmos de recomendación. Se generaron datos sintéticos para superar la falta de datos suficientes y se integraron los resultados en MongoDB.

**Algoritmos y métodos:**

-   **Filtrado Colaborativo Basado en Usuarios:** Se calculó la similitud del coseno entre las interacciones de los usuarios y se recomendaron productos que otros usuarios similares han interactuado.
    
-   **Filtrado Colaborativo Basado en Ítems:** Se calculó la similitud del coseno entre los productos basándose en las interacciones de los usuarios y se recomendaron productos similares a los que el usuario ya ha consumido.
    
-   **Clustering de Usuarios utilizando K-means:** Se agruparon los usuarios en clusters basados en sus interacciones y se generaron recomendaciones basadas en los productos más populares dentro del cluster.
    

**Desafíos encontrados:** Durante el desarrollo, se encontraron desafíos relacionados con la falta de datos suficientes y la necesidad de generar datos sintéticos. Además, se enfrentaron problemas de eficiencia en la integración de los algoritmos con MongoDB, que se resolvieron optimizando las consultas y la estructura de la base de datos.

#### 4. Resultados

**Funcionalidades desarrolladas:**

-   Recomendaciones basadas en la similitud entre usuarios
-   Recomendaciones basadas en la similitud entre ítems
-   Recomendaciones basadas en clusters de usuarios
-   Integración de los resultados de las recomendaciones con MongoDB

**Pruebas realizadas:** Se realizaron pruebas unitarias y de integración para asegurar el correcto funcionamiento de los algoritmos implementados. También se llevaron a cabo pruebas de rendimiento para evaluar la eficiencia de las recomendaciones generadas.



![image.png](https://i.postimg.cc/ry0rp5RQ/image.png)



- **Explicación de los Resultados**


	- **Recomendaciones Basadas en Usuarios**: Se muestran los productos recomendados para el usuario 'user_1' basándose en la similitud con otros usuarios. Los productos recomendados son ['producto_27', 'producto_32', 'producto_10', 'producto_28', 'producto_43'].


	- **Recomendaciones Basadas en Ítems**: Se muestran los productos recomendados para el usuario 'user_1' basándose en la similitud con otros productos que el usuario ha interactuado. Los productos recomendados son ['producto_1', 'producto_9', 'producto_35', 'producto_12', 'producto_33'].


	- **Resultados de Evaluación**: Las métricas de evaluación indican que las recomendaciones son precisas (precisión de 1.0), pero la cobertura (recall) y el equilibrio entre precisión y recall (F1-Score) son más bajos, indicando áreas de mejora en términos de cobertura de las recomendaciones.

# Clustering de Usuarios 

**Clustering de Usuarios utilizando K-means**

Se implementó el algoritmo de clustering K-means para agrupar usuarios en clusters basados en sus interacciones. Las recomendaciones se generaron basándose en los productos más populares dentro del cluster al que pertenece el usuario.



![image.png](https://i.postimg.cc/SQMn4qHP/image.png)



- **Explicación de los Resultados de Clustering**


- **Recomendaciones Basadas en Clusters**: Se muestran los productos recomendados para el usuario 'user_1' basándose en los productos más populares dentro del cluster al que pertenece el usuario. Los productos recomendados en este caso son ['producto_44', 'producto_26', 'producto_40', 'producto_38', 'producto_13'].


- **Resultados de Evaluación**: Las métricas de evaluación muestran que el algoritmo de clustering tiene una precisión alta (1.00), pero un recall y F1-score más bajos en comparación con el filtrado colaborativo basado en usuarios e ítems. Esto sugiere que el clustering es útil pero podría beneficiarse de mejoras adicionales para aumentar la cobertura de las recomendaciones.

# Integración de los Algoritmos

Se integraron los algoritmos de recomendación con MongoDB para obtener datos de usuarios y productos en tiempo real. Además, se almacenaron los resultados de las recomendaciones en la base de datos para su posterior análisis y validación.



![image.png](https://i.postimg.cc/jj2jFrzZ/image.png)



**Explicación de los Resultados de Integración**

- **Recomendaciones Basadas en Usuarios**: Productos recomendados basándose en la similitud entre usuarios. Los productos recomendados son ['producto_27', 'producto_32', 'producto_10', 'producto_28', 'producto_43'].


- **Recomendaciones Basadas en Ítems**: Productos recomendados basándose en la similitud entre ítems. Los productos recomendados son ['producto_1', 'producto_9', 'producto_35', 'producto_12', 'producto_33'].


- **Recomendaciones Basadas en Clusters**: Productos recomendados basándose en la popularidad dentro del cluster del usuario. Los productos recomendados son ['producto_5', 'producto_1', 'producto_28', 'producto_40', 'producto_32'].


- **Resultados de Evaluación**: La evaluación conjunta muestra que el filtrado colaborativo basado en usuarios y el enfoque híbrido proporcionan el mejor equilibrio entre precisión y cobertura. El filtrado basado en ítems y clustering tienen un rendimiento ligeramente inferior en términos de recall y F1-score, pero aún así son útiles como métodos complementarios.


**Comparación de algoritmos**


- **Filtrado Colaborativo Basado en Usuarios:** Ofreció la mayor cobertura (recall) y una buena precisión, proporcionando recomendaciones relevantes basadas en la similitud entre usuarios.


- **Filtrado Colaborativo Basado en Ítems:** Fue menos efectivo en términos de recall comparado con el enfoque basado en usuarios, pero aún así proporcionó recomendaciones relevantes.


- **Recomendaciones Híbridas:** Combinó los beneficios de ambos enfoques de filtrado colaborativo, ofreciendo una cobertura y precisión balanceadas.


- **Clustering:** Aunque tuvo una precisión perfecta, su recall fue más bajo en comparación con los enfoques de filtrado colaborativo, indicando que no pudo capturar todas las interacciones relevantes.


# Errores durante el sprint 2

El Motivo de la Generación de Datos Sintéticos Durante el desarrollo del Sprint 2, se observó una falta de datos suficientes en las interacciones y los productos. Para abordar esta deficiencia, se generaron datos sintéticos adicionales utilizando el script datos_sinteticos.py. Esto permitió aumentar el volumen de datos de entrenamiento y mejorar la precisión y robustez de los algoritmos de recomendación*.


# Visión General de la Base de Datos

En las imágenes se muestra la estructura de la base de datos MongoDB utilizada en el proyecto. La base de datos está organizada en varias colecciones:

- interacciones: Almacena las interacciones de los usuarios con los productos. En este caso, hay 1000 documentos.

- productos: Contiene la información de los productos. Hay 50 documentos en esta colección.

- recomendaciones_usuario: Almacena las recomendaciones generadas para cada usuario. Hay 3 documentos que corresponden a las recomendaciones generadas para tres usuarios diferentes.

- usuarios: Contiene información sobre los usuarios. Hay 100 documentos en esta colección.



![image.png](https://i.postimg.cc/rFhXYRQ2/image.png)



**Detalle de la Colección recomendaciones_usuario**

En la colección recomendaciones_usuario, se almacena la siguiente información para cada usuario:

- user_id: Identificador del usuario.

- recomendaciones_usuario: Lista de productos recomendados basados en la similitud entre usuarios.

- recomendaciones_items: Lista de productos recomendados basados en la similitud entre ítems.

- recomendaciones_cluster: Lista de productos recomendados utilizando técnicas de clustering.

- recomendaciones_hibridas: Lista de productos recomendados utilizando un enfoque híbrido.



![image.png](https://i.postimg.cc/W39wPVKz/image.png)




Las imágenes muestran que se han implementado y almacenado correctamente las recomendaciones generadas por los diferentes algoritmos en la base de datos MongoDB. Esto demuestra la integración exitosa del sistema de recomendación con la base de datos.

-   **Recomendaciones basadas en usuarios:** Basadas en la similitud entre usuarios, se recomienda productos que otros usuarios similares han consumido.
-   **Recomendaciones basadas en ítems:** Basadas en la similitud entre productos, se recomienda productos similares a los que el usuario ya ha consumido.
-   **Recomendaciones basadas en clusters:** Utilizando técnicas de clustering, se agrupan usuarios y se generan recomendaciones basadas en las interacciones dentro de cada cluster.



#### 5. Análisis y evaluación

**Comparación con los objetivos del Sprint:** El trabajo realizado durante el sprint cumplió con los objetivos establecidos. Los algoritmos implementados funcionan correctamente y se integraron con éxito en la base de datos.

**Lecciones aprendidas:**

-   La generación de datos sintéticos fue crucial para asegurar suficientes datos para el entrenamiento y la evaluación de los algoritmos.
-   La integración con MongoDB y la optimización de las consultas son esenciales para el rendimiento del sistema de recomendación.


#### 6. Plan para el próximo Sprint

**Objetivos del próximo Sprint:**

-   Optimizar el rendimiento del sistema de recomendación utilizando técnicas de paralelismo
-   Preparar y presentar los resultados del proyecto

**Tareas planificadas:**

-   Identificar cuellos de botella en el rendimiento
-   Implementar técnicas de paralelismo utilizando `multiprocessing` y `threading`
-   Optimizar consultas a MongoDB
-   Realizar pruebas de carga
-   Implementar herramientas de monitoreo y logging
