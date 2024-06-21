# MEJORA SPRINT 1

Durante el desarrollo del Sprint 1, se identificaron ciertas áreas de mejora que eran necesarias para alcanzar los objetivos del proyecto de manera más efectiva. En particular, se necesitaba un mayor volumen de datos de interacciones y usuarios para garantizar la robustez y precisión del sistema de recomendación.

#### Dataset Utilizado

Para abordar estas necesidades, se decidió utilizar el **Retailrocket Dataset**, un conjunto de datos extensivo y específico del ámbito del comercio electrónico. Este dataset incluye una variedad rica de interacciones entre usuarios y productos, así como una amplia gama de información sobre productos y usuarios.

#### Motivo de la Elección

El **Retailrocket Dataset** fue elegido debido a las siguientes razones:

1.  **Volumen de Datos**: Este dataset proporciona una cantidad significativa de datos, incluyendo miles de interacciones, lo que es crucial para entrenar y evaluar modelos de recomendación.
2.  **Diversidad de Interacciones**: Incluye diversos tipos de interacciones como clics, vistas y compras, permitiendo un análisis más completo y realista del comportamiento del usuario.
3.  **Detalles de Productos y Categorías**: Proporciona información detallada sobre productos y sus categorías, lo que es esencial para las técnicas de filtrado colaborativo y clustering.

#### Pasos Realizados en el Sprint 1 con el Nuevo Dataset


1.  **Análisis de Requisitos y Diseño de la Base de Datos**:
    
    -   **Tipos de Datos**: Se identificaron los tipos de datos necesarios, incluyendo información de usuarios, productos e interacciones.
    -   **Estructura de la Base de Datos**: Se diseñó la estructura de la base de datos, definiendo las colecciones y los documentos necesarios.
    -   **Documentación del Esquema**: Se documentó el esquema de la base de datos, especificando las relaciones y los índices necesarios para optimizar las consultas.
    
    
2.  **Configuración de MongoDB**:
    
    -   **Instalación y Configuración**: Se instaló y configuró MongoDB en el entorno de desarrollo.
    -   **Creación de Colecciones**: Se crearon las colecciones para usuarios, productos e interacciones.
    -   **Definición de Índices**: Se definieron índices en las colecciones para mejorar el rendimiento de las consultas.
    
    
3.  **Población de la Base de Datos**:
    
    -   **Obtención de Datos**: Se utilizaron los primeros 500 registros de los archivos CSV del **Retailrocket Dataset** para poblar la base de datos.
    -   **Inserción de Datos**: Se insertaron los datos en las colecciones correspondientes de MongoDB.
    -   **Validación de Datos**: Se validó la integridad y consistencia de los datos insertados mediante consultas de prueba.



![image.png](https://i.postimg.cc/90BcjC1j/image.png)

### Explicación del Esquema

1.  **Usuarios**:
    
    -   `_id`: Identificador único de MongoDB para cada documento.
    -   `user_id`: Identificador único del usuario.
    -   `name`: Nombre del usuario.
    -   `email`: Correo electrónico del usuario.
    -   `age`: Edad del usuario.
    -   `gender`: Género del usuario.
    -   `location`: Ubicación del usuario.
2.  **Productos**:
    
    -   `_id`: Identificador único de MongoDB para cada documento.
    -   `product_id`: Identificador único del producto.
    -   `category_id`: Identificador de la categoría a la que pertenece el producto.
    -   `category_name`: Nombre de la categoría del producto.
3.  **Interacciones**:
    
    -   `_id`: Identificador único de MongoDB para cada documento.
    -   `user_id`: Identificador del usuario que interactúa con el producto.
    -   `product_id`: Identificador del producto con el que se interactúa.
    -   `interaction_type`: Tipo de interacción (por ejemplo, clic, vista, compra).
    -   `timestamp`: Fecha y hora de la interacción.

### Relación entre las Colecciones

-   **usuarios -> interacciones**: Un usuario puede tener muchas interacciones.
-   **productos -> interacciones**: Un producto puede tener muchas interacciones.


### Conclusión

El uso del **Retailrocket Dataset** mejoró significativamente el Sprint 1, permitiendo la creación de un sistema de recomendación más robusto y preciso. Al proporcionar un mayor volumen y diversidad de datos, se lograron resultados más efectivos en las recomendaciones y se sentaron las bases para las actividades del Sprint 2.
