### Sprint 3: Optimización del Sistema de Recomendación Utilizando Técnicas de Paralelismo

## 1. Introducción

**Objetivos del Sprint:** El objetivo principal del Sprint 3 fue optimizar el rendimiento del sistema de recomendación mediante la implementación de técnicas de paralelismo y caching. Esto incluye identificar cuellos de botella, mejorar tiempos de procesamiento, realizar pruebas de carga, y configurar herramientas de monitoreo y logging para supervisar el rendimiento del sistema en tiempo real. También se buscó documentar todo el proceso en el repositorio de GitHub.

## 2. Planificación

**Tareas planificadas:**

-   Identificación de cuellos de botella en el sistema.
-   Implementación de técnicas de paralelismo con `multiprocessing` y `threading`.
-   Optimización de consultas a MongoDB.
-   Implementación de Redis como sistema de caché.
-   Realización de pruebas de carga con Locust.
-   Configuración de herramientas de monitoreo (Prometheus y Grafana, EKL stack ).
-   Documentación y preparación de la presentación final.


## 3. Implementación

**Descripción del trabajo realizado:** Durante este sprint, se identificaron los principales cuellos de botella del sistema, específicamente en tiempos de consulta a la base de datos y procesamiento de algoritmos de recomendación. Se implementaron técnicas de paralelismo utilizando `multiprocessing` y `threading`, y se optimizaron las consultas a MongoDB con índices adecuados. Además, se implementó Redis como sistema de caché para reducir la carga en la base de datos y mejorar los tiempos de respuesta. Finalmente, se realizaron pruebas de carga con Locust y se configuraron herramientas de monitoreo como Prometheus y Grafana.


**Algoritmos y métodos:**

- **Paralelismo con `multiprocessing` y `threading`:**

integracion.py
```python
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

class Recomendador:
    def calcular_y_almacenar_recomendaciones(self, user_ids):
        with ProcessPoolExecutor() as executor:
            resultados = list(executor.map(self.calcular_recomendaciones, user_ids))

        with ThreadPoolExecutor() as executor:
            resultados_cluster = list(executor.map(self.recomendar_productos_cluster, user_ids, [self.user_product_matrix_train]*len(user_ids)))
        
        recomendaciones = []
        for user_id, (rec_user, rec_item, rec_hib), rec_cluster in zip(user_ids, resultados, resultados_cluster):
            recomendaciones.append({
                'user_id': user_id,
                'recomendaciones_usuario': rec_user.to_dict(),
                'recomendaciones_items': rec_item.to_dict(),
                'recomendaciones_hibrido': rec_hib.to_dict(),
                'recomendaciones_cluster': rec_cluster.to_dict()
            })
        self.db.recomendaciones_totales.insert_many(recomendaciones)
  ```


- **Implementación de Redis para caching:**

app.py
 ```python
import redis

class Recomendador:
    def __init__(self):
        self.redis_client = redis.StrictRedis(host='redis', port=6379, db=0)
        # ... Resto del código de inicialización

    def get_recommendations_from_cache(self, user_id):
        cache_key = f"recommendations:{user_id}"
        return self.redis_client.get(cache_key)
    
    def set_recommendations_to_cache(self, user_id, recommendations):
        cache_key = f"recommendations:{user_id}"
        self.redis_client.setex(cache_key, 3600, recommendations)
 ```

**Desafíos encontrados:**

-   Configuración y conexión inicial con Redis.
-   Sincronización de procesos y manejo de estados compartidos en paralelismo.
-   Manejo de grandes volúmenes de datos durante las pruebas de carga.

## 4. Resultados

**Funcionalidades desarrolladas:**

-   Optimización del sistema de recomendación con técnicas de paralelismo.
-   Implementación de Redis como sistema de caché.
-   Pruebas de carga y configuración de herramientas de monitoreo.

## 5. Análisis y evaluación

**Comparación con los objetivos del Sprint:** Los objetivos iniciales del sprint se cumplieron exitosamente. Se mejoró significativamente el rendimiento del sistema de recomendación mediante la implementación de técnicas de paralelismo y caching. Las pruebas de carga demostraron una mejora notable en los tiempos de respuesta y la escalabilidad del sistema.

**Lecciones aprendidas:**

-   El uso de Redis como sistema de caché puede reducir significativamente los tiempos de respuesta y la carga en la base de datos.
-   La implementación de técnicas de paralelismo puede mejorar la eficiencia del procesamiento de datos, pero requiere una cuidadosa gestión de los recursos y la sincronización.
-   Las herramientas de monitoreo y logging son esenciales para identificar y resolver problemas de rendimiento de manera proactiva.


### Sin uso de Redis
![prueba1.png](https://i.postimg.cc/nhwNC7zW/prueba1.png)



### Uso de Redis
![prueba1-redis.png](https://i.postimg.cc/wvz2vThP/prueba1-redis.png)


#### Análisis Comparativo y Conclusiones

-   **Request Statistics:**
    
    -   **Sin Redis:** La aplicación tuvo 2958 solicitudes con 101 fallos. El tiempo medio de respuesta fue extremadamente alto (37540.86 ms), lo que indica un rendimiento lento y poco eficiente bajo carga.
    -   **Con Redis:** La aplicación manejó significativamente más solicitudes (11774) sin ningún fallo. El tiempo medio de respuesta se redujo drásticamente a 8.31 ms.
-   **Response Time Statistics:**
    
    -   **Sin Redis:** La mediana y los percentiles de los tiempos de respuesta fueron altos, con un 50% de las solicitudes tomando 41000 ms o más. Esto muestra que la aplicación no pudo manejar la carga de manera eficiente.
    -   **Con Redis:** Los tiempos de respuesta mejoraron notablemente, con la mayoría de las solicitudes respondiendo en menos de 10 ms. Esto indica que Redis ayudó a reducir la latencia de manera significativa.
-   **Failures Statistics:**
    
    -   **Sin Redis:** Se observaron errores de tiempo de espera y restablecimiento de conexión, lo que sugiere que la aplicación no pudo mantener la estabilidad bajo una carga más alta.
    -   **Con Redis:** No hubo fallos registrados, lo que indica una mejora significativa en la estabilidad y el manejo de la carga.

**Conclusión:** La implementación de Redis para caching tuvo un impacto positivo significativo en el rendimiento del sistema de recomendación. Los tiempos de respuesta mejoraron drásticamente y la aplicación pudo manejar una carga mucho mayor sin fallos. Esto demuestra que el uso de Redis como mecanismo de cacheo puede mejorar considerablemente la eficiencia y escalabilidad de aplicaciones que requieren acceso rápido a datos frecuentemente consultados.


### Monitoreo con Grafana, Prometheus y EKL stack


### Grafana - app_request_count_total 
![app-request-count-total.png](https://i.postimg.cc/LsLyS4Cq/app-request-count-total.png)


Esta imagen muestra el panel de Grafana monitoreando la métrica `app_request_count_total`, que indica el número total de solicitudes realizadas a la aplicación Flask. Los picos en el gráfico representan momentos en los que se hicieron muchas solicitudes simultáneamente.

**Puntos Clave:**

-   La métrica se incrementa cada vez que se recibe una solicitud en el endpoint `/recomendaciones`.
-   Los intervalos con picos indican alta actividad en la aplicación, lo que puede ayudar a identificar períodos de alta carga.
-   El monitoreo en tiempo real permite detectar rápidamente cualquier anomalía en la tasa de solicitudes.


### ElasticSearch Discover - flask-app-logs
![Captura-desde-2024-07-01-20-04-33.png](https://i.postimg.cc/ncNNBhWz/Captura-desde-2024-07-01-20-04-33.png)

Esta imagen muestra el descubrimiento de logs en Kibana para el índice `flask-app-logs`. Se puede observar una lista de registros que contienen información detallada sobre las solicitudes procesadas por la aplicación.

**Puntos Clave:**

-   Cada registro contiene campos como `user_id`, `timestamp`, `message`, etc., que proporcionan información valiosa sobre cada solicitud.
-   Los histogramas en la parte superior muestran la distribución de logs a lo largo del tiempo, permitiendo identificar picos de actividad.
-   El análisis de logs ayuda a diagnosticar problemas y a entender el comportamiento de la aplicación bajo diferentes cargas.



### Grafana - Logs Count
![Captura-desde-2024-07-01-15-13-13.png](https://i.postimg.cc/dVX38w9V/Captura-desde-2024-07-01-15-13-13.png)

-   El gráfico de líneas muestra la cantidad de logs generados por la aplicación en intervalos de 20 ms.
-   Los picos en el gráfico indican momentos de alta actividad en la generación de logs, que pueden correlacionarse con los picos de solicitudes observados en la primera imagen.
-   Este monitoreo es crucial para entender la eficiencia de la aplicación y detectar posibles problemas de rendimiento o errores.



### Conclusión

El monitoreo de métricas y logs es esencial para comprender el rendimiento y comportamiento de la aplicación en tiempo real. A través de Grafana y Kibana, hemos podido identificar picos de actividad y analizar detalladamente los registros de la aplicación. Este proceso ha sido crucial para optimizar el sistema, implementar mejoras y garantizar su escalabilidad y rendimiento bajo diferentes condiciones de carga.
