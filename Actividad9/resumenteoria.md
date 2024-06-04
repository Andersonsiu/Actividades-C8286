##Arquitecturas de Sistemas Paralelos##

1. Arquitectura de Memoria Compartida
En una arquitectura de memoria compartida, todos los procesadores acceden a un único espacio de memoria global. Este tipo de arquitectura facilita la programación debido a la comunicación y sincronización a través de variables compartidas.
Tipos de Memoria Compartida:
•	Memoria Compartida Uniforme (UMA):
•	Todos los procesadores tienen el mismo tiempo de acceso a la memoria principal.
•	Ejemplos: Estaciones de trabajo multiprocesador, servidores de gama media.
•	Ventajas: Simplicidad en la programación y facilidad en la coherencia de caché.
•	Desventajas: No escala bien con un gran número de procesadores debido a la contención de memoria y cuellos de botella en el bus de memoria.
•	Memoria Compartida No Uniforme (NUMA):
•	Cada procesador tiene su memoria local y el tiempo de acceso varía según la memoria accedida (local o remota).
•	Ejemplos: Servidores de alto rendimiento, sistemas NUMA como AMD EPYC e Intel Xeon.
•	Ventajas: Mejor escalabilidad y acceso más rápido a la memoria local.
•	Desventajas: Mayor complejidad en la programación debido a la latencia variable en el acceso a la memoria.
Ventajas y Desventajas de la Memoria Compartida:
•	Ventajas:
•	Facilidad de programación.
•	Rendimiento optimizado en sistemas UMA.
•	Gestión de coherencia de caché.
•	Desventajas:
•	Limitaciones de escalabilidad en sistemas UMA.
•	Complejidad en NUMA.
•	Costos más altos debido a hardware sofisticado.
2. Arquitectura de Memoria Distribuida
En una arquitectura de memoria distribuida, cada procesador tiene su propia memoria local y la comunicación entre procesadores se realiza mediante el paso de mensajes.
Tipos de Arquitecturas de Memoria Distribuida:
•	Multicomputadores:
•	Sistemas compuestos por varios nodos de computación, cada uno con su propia CPU y memoria, interconectados mediante una red de alta velocidad.
•	Ejemplos: Supercomputadoras, clústeres de computadoras.
•	Ventajas: Alta escalabilidad y mejor tolerancia a fallos.
•	Desventajas: Programación más compleja debido a la gestión de la comunicación y sincronización entre nodos.
•	Clústeres de Computadoras:
•	Varios sistemas completos (nodos) conectados a través de una red para trabajar juntos como un solo sistema.
•	Ejemplos: Clústeres de alto rendimiento (HPC), clústeres de alta disponibilidad (HA).
•	Ventajas: Coste-efectividad y capacidad de combinar recursos de diferentes sistemas.
•	Desventajas: Dependencia de la red para la comunicación, lo que puede introducir latencias significativas.
Ventajas y Desventajas de la Memoria Distribuida:
•	Ventajas:
•	Escalabilidad.
•	Tolerancia a fallos.
•	Flexibilidad para integrar diferentes tipos de hardware.
•	Desventajas:
•	Complejidad en la programación.
•	Latencia de comunicación entre nodos.
3. Arquitecturas Paralelas Híbridas
Las arquitecturas híbridas combinan elementos de arquitecturas de memoria compartida y distribuida para aprovechar las ventajas de ambas y mitigar sus desventajas.
Ejemplo de Arquitectura Híbrida:
•	Clúster de Nodos NUMA:
•	Cada nodo es un sistema NUMA con múltiples procesadores y memoria local.
•	Los nodos están conectados a través de una red de alta velocidad, formando un sistema de memoria distribuida.
Ventajas de las Arquitecturas Híbridas:
•	Escalabilidad mejorada.
•	Flexibilidad para una amplia variedad de aplicaciones.
•	Rendimiento mejorado gracias al acceso rápido a la memoria local.
•	Tolerancia a fallos.
Desventajas de las Arquitecturas Híbridas:
•	Complejidad de programación.
•	Latencia de comunicación entre nodos.
•	Costos elevados debido a hardware y redes sofisticadas.
Modelos de Programación en Arquitecturas Híbridas:
•	MPI+OpenMP: Combinación de paso de mensajes y memoria compartida.
•	UPC (Unified Parallel C): Modelo que extiende C para incluir memoria compartida y distribuida.
•	GASNet (Global Address Space Networking): API para modelos de programación con espacio de direcciones global.
Aplicaciones Adecuadas
•	Memoria Compartida:
•	Alta interactividad entre procesos.
•	Facilidad de programación.
•	Necesidad crítica de coherencia de caché y sincronización.
•	Memoria Distribuida:
•	Alta escalabilidad (simulaciones científicas, análisis de big data).
•	Tolerancia a fallos.
•	Aplicaciones que pueden tolerar latencias de comunicación más altas.
Ejemplo de Clúster HPC Híbrido
•	Interconexión de alta velocidad: Red InfiniBand para baja latencia y alto ancho de banda.
•	Gestión de memoria eficiente: Uso de memoria local para datos de acceso frecuente y memoria distribuida para otros datos.
•	Soporte para diversos modelos de programación: Flexibilidad para desarrolladores.
•	Escalabilidad y rendimiento: Capacidad de escalar a miles de nodos para aplicaciones de gran escala.
Técnicas de Computación Paralela y Distribuida
•	Paralelismo de Datos: Dividir grandes conjuntos de datos en partes más pequeñas para procesarlas simultáneamente.
•	Paralelismo de Tareas: Dividir un programa en tareas o hilos que se ejecutan en paralelo.
•	Modelos de Programación Paralela:
•	Modelo de paso de mensajes (MPI): Utilizado en sistemas de memoria distribuida.
•	Modelo de memoria compartida (OpenMP): Utilizado en sistemas de memoria compartida.
•	Modelo híbrido: Combinación de MPI y OpenMP para aprovechar las ventajas de ambos en sistemas NUMA o clústeres heterogéneos.



##Memoria Caché##
Definición y Importancia
La memoria caché es una memoria de alta velocidad que almacena temporalmente los datos más utilizados, mejorando significativamente el rendimiento del sistema al reducir el tiempo de acceso a los datos. Es esencial en la arquitectura de los sistemas modernos, especialmente en la programación paralela y distribuida, donde una gestión eficiente de la caché es crucial para maximizar el rendimiento y minimizar la latencia.
Tamaños de Caché L1, L2, L3
1.	Caché L1:
•	Ubicación: Más cercana al núcleo del procesador.
•	División: Caché de instrucciones (L1i) y caché de datos (L1d).
•	Tamaño: 32KB a 64KB por núcleo.
•	Latencia: Muy baja, unos pocos ciclos de reloj.
2.	Caché L2:
•	Ubicación: Más grande y ligeramente más lenta que L1.
•	Configuración: Cada núcleo puede tener su propia caché L2 o compartirla.
•	Tamaño: 256KB a 512KB por núcleo.
•	Latencia: Generalmente entre 10 y 20 ciclos de reloj.
3.	Caché L3:
•	Ubicación: Compartida entre todos los núcleos de un procesador.
•	Tamaño: 2MB a 32MB o más.
•	Latencia: Entre 30 y 50 ciclos de reloj.
Políticas de Reemplazo de Caché
1.	Least Recently Used (LRU): Reemplaza el bloque que no ha sido usado por más tiempo.
2.	First In, First Out (FIFO): Reemplaza el bloque más antiguo.
3.	Least Frequently Used (LFU): Reemplaza el bloque usado con menor frecuencia.
4.	Random Replacement: Reemplaza un bloque al azar.
Latencia de Caché
La latencia de la caché es el tiempo que tarda el procesador en acceder a los datos almacenados en ella. La baja latencia de la caché L1 permite operaciones rápidas, mientras que las cachés L2 y L3 tienen latencias mayores, afectando el rendimiento si los datos no están presentes en las cachés de nivel superior.
Gestión de Caché en Programación Paralela y Distribuida
1.	Localidad de Referencia: Optimizar los algoritmos para mejorar la localidad temporal y espacial.
2.	Afinidad de Núcleo: Asignar tareas a núcleos específicos y mantener la afinidad de los datos a esos núcleos.
3.	Coherencia de Caché: Usar protocolos como MESI y MOESI para asegurar la coherencia de la memoria.
4.	Prefetching: Cargar datos en la caché antes de que sean necesitados.
5.	Particionado de Caché: Dividir la caché en segmentos asignados a diferentes núcleos o procesos.
6.	Optimización de Algoritmos: Adaptar los algoritmos para ser más "cache-friendly".
Coherencia de Caché
Concepto
La coherencia de caché asegura que todas las copias de una misma ubicación de memoria, almacenadas en las cachés de distintos procesadores, mantengan valores consistentes.
Protocolos de Coherencia
1.	MESI (Modified, Exclusive, Shared, Invalid):
•	Modificado: Línea de caché ha sido alterada y no es coherente con la memoria principal.
•	Exclusivo: Línea de caché es la única copia y es coherente con la memoria principal.
•	Compartido: Línea de caché puede estar en múltiples cachés y es coherente con la memoria principal.
•	Inválido: Línea de caché no es válida.
2.	MOESI (Modified, Owner, Exclusive, Shared, Invalid):
•	Introduce el estado Owned: Una copia modificada que puede ser compartida.
3.	MSI (Modified, Shared, Invalid): Versión simplificada de MESI.
Mecanismos de Consistencia
1.	Snooping: Todas las cachés observan el bus para detectar operaciones relevantes.
2.	Directorios: Mantienen un registro del estado de cada línea de caché en todas las cachés del sistema.
Consistencia de Caché
Modelos de Consistencia
1.	Consistencia Secuencial: Operaciones de memoria se ven en el orden en que se ejecutaron.
2.	Consistencia Débil: Operaciones de memoria pueden ejecutarse en cualquier orden, con sincronización en puntos específicos.
3.	Consistencia de Memoria Liberada: Operaciones de lectura y escritura pueden realizarse en cualquier orden, pero las operaciones de sincronización deben ejecutarse en un orden específico.
Desafíos en Sistemas Distribuidos
•	Latencia de Red: Mayor latencia en la comunicación entre nodos distribuidos.
•	Cachés Distribuidas: Replicación de datos para mejorar el rendimiento y disponibilidad.
•	Algoritmos de Consenso: Usar Paxos y Raft para asegurar la consistencia de datos en presencia de fallos.

