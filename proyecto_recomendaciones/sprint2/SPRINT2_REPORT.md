# Introducción

El objetivo del Sprint 2 fue implementar un sistema de recomendación basado en técnicas de filtrado colaborativo y clustering para mejorar la precisión de las recomendaciones. Además, se buscó evaluar la eficacia de estos algoritmos utilizando métricas estándar y almacenar los resultados en una base de datos MongoDB.

**Objetivos**

- Desarrollar algoritmos de recomendación basados en filtrado colaborativo.

- Implementar técnicas de clustering para mejorar las recomendaciones.

- Evaluar la precisión y cobertura de los algoritmos.
Integrar los algoritmos de recomendación con MongoDB para obtener y almacenar datos en tiempo real.


# Filtrado Colaborativo

- **Filtrado Colaborativo Basado en Usuarios (User-Based Collaborative Filtering)**

Se implementó un algoritmo de filtrado colaborativo basado en la similitud entre usuarios para recomendar productos. Este algoritmo calcula la similitud del coseno entre las interacciones de los usuarios y recomienda productos que otros usuarios similares han interactuado.


- **Filtrado Colaborativo Basado en Ítems (Item-Based Collaborative Filtering)**

Se implementó un algoritmo de filtrado colaborativo basado en la similitud entre ítems para recomendar productos. Este algoritmo calcula la similitud del coseno entre los productos basándose en las interacciones de los usuarios y recomienda productos que son similares a los que el usuario ya ha consumido.



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




# Conclusión

La implementación del sistema de recomendación ha sido exitosa, integrando algoritmos de filtrado colaborativo y clustering. Los resultados generados han sido almacenados correctamente en la base de datos MongoDB, permitiendo así una gestión eficiente y en tiempo real de las recomendaciones. La adición de datos sintéticos ha sido crucial para asegurar que los algoritmos tuvieran suficiente información para entrenarse y evaluarse de manera efectiva, mostrando que el sistema puede adaptarse a diferentes cantidades de datos y seguir funcionando correctamente.
