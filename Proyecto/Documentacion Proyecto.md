# Entregables:

- Diseño documentado del esquema de la base de datos.

- Base de datos MongoDB configurada con colecciones e índices definidos.

- Datos de usuarios, productos e interacciones insertados y validados en la base de datos.


1. Diseño Documentado del Esquema de la Base de Datos


# Diagrama del Esquema de la Base de Datos:


![image.png](https://i.postimg.cc/xTxfbrVk/image.png)



# Colección de Usuarios

- **user_id**: String - Identificador único del usuario.
- **nombre**: String - Nombre del usuario.
- **email**: String - Correo electrónico del usuario.
- **fecha_registro**: Date - Fecha en la que el usuario se registró.
- **preferencias**: Array of Strings - Lista de preferencias del usuario.
- **historial_compras**: Array of Objects - Historial de compras del usuario, cada objeto contiene:
  - **producto_id**: String
  - **fecha**: Date
  - **cantidad**: Integer
- **actividad_navegacion**: Array of Objects - Actividad de navegación del usuario, cada objeto contiene:
  - **producto_id**: String
  - **fecha**: Date
  - **tipo_interaccion**: String

# Colección de Productos

- **producto_id**: String - Identificador único del producto.
- **nombre**: String - Nombre del producto.
- **categoría**: String - Categoría a la que pertenece el producto.
- **precio**: Decimal - Precio del producto.
- **descripcion**: String - Descripción del producto.
- **calificaciones**: Array of Objects - Calificaciones del producto, cada objeto contiene:
  - **user_id**: String
  - **calificación**: Integer
- **disponibilidad**: Boolean - Disponibilidad del producto.
- **especificaciones**: Object - Especificaciones adicionales del producto en formato clave-valor.

# Colección de Interacciones

- **interaccion_id**: String - Identificador único de la interacción.
- **user_id**: String - Identificador del usuario que realizó la interacción (referencia a Usuarios).
- **producto_id**: String - Identificador del producto involucrado en la interacción (referencia a Productos).
- **tipo_interaccion**: String - Tipo de interacción (por ejemplo, "click", "compra", "review").
- **fecha**: Date - Fecha de la interacción.
- **detalle_interaccion**: Object - Detalle adicional de la interacción en formato clave-valor (opcional).

# Relaciones Lógicas

1. **Usuarios <--- user_id --- Interacciones**:
   - **user_id** en la colección Interacciones referencia a **user_id** en la colección Usuarios.
   - Esto indica que cada interacción está asociada a un usuario específico.

2. **Productos <--- producto_id --- Interacciones**:
   - **producto_id** en la colección Interacciones referencia a **producto_id** en la colección Productos.
   - Esto indica que cada interacción está asociada a un producto específico.



# 2. Base de Datos MongoDB Configurada**

**Pasos para Configurar MongoDB y Crear las Colecciones e Índices**:


![image.png](https://i.postimg.cc/QCSfdkP7/image.png)



**Índice en email (usuarios)**: Garantiza unicidad y permite búsquedas rápidas por correo electrónico.

**Índice Compuesto en user_id y producto_id (interacciones)**: Optimiza consultas que filtran por usuario y producto.

**Índice de Texto en nombre y descripcion (productos)**: Mejora búsquedas de productos por texto en nombre y descripción.


# 3. Datos de Ejemplo Insertados y Validados:

![image.png](https://i.postimg.cc/8C1shRnc/image.png)



![image.png](https://i.postimg.cc/CMWGb2CK/image.png)



![image.png](https://i.postimg.cc/nVQ7Vk8f/image.png)


# Validación de los Datos Insertados:


![image.png](https://i.postimg.cc/VvcNkXMz/image.png)


**Verificación desde la consola:**



![image.png](https://i.postimg.cc/cLj0JQyP/image.png)
