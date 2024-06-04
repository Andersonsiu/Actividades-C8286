from collections import deque

class FIFOCache:
    def __init__(self, capacity):
        self.capacity = capacity  # Capacidad máxima de la caché
        self.cache = {}  # Diccionario para almacenar los datos de la caché
        self.order = deque()  # Deque para mantener el orden de inserción de las claves

    def get(self, key):
        # Devuelve el valor asociado a la clave, o -1 si la clave no está en la caché
        return self.cache.get(key, -1)

    def put(self, key, value):
        if key not in self.cache:
            # Si la caché ha alcanzado su capacidad, elimina el elemento más antiguo
            if len(self.cache) >= self.capacity:
                oldest = self.order.popleft()  # Elimina la clave más antigua de la deque
                del self.cache[oldest]  # Elimina la clave más antigua del diccionario
            self.cache[key] = value  # Añade el nuevo elemento al diccionario de la caché
            self.order.append(key)  # Añade la nueva clave al final de la deque
        else:
            # Si la clave ya está en la caché, actualiza su valor
            self.cache[key] = value

# Simulación de acceso a la caché
cache = FIFOCache(3)
operations = [
    ("put", 1, "data1"), 
    ("put", 2, "data2"), 
    ("put", 3, "data3"), 
    ("get", 1),
    ("put", 4, "data4"), 
    ("get", 2), 
    ("put", 5, "data5"), 
    ("get", 3), 
    ("get", 1)
]

# Ejecuta las operaciones y muestra el estado de la caché después de cada una
for op in operations:
    if op[0] == "put":
        # Realiza la operación 'put' con la clave y el valor especificados
        cache.put(op[1], op[2])
        print(f"Put: {op[1]} -> {op[2]}")
    elif op[0] == "get":
        # Realiza la operación 'get' con la clave especificada
        result = cache.get(op[1])
        print(f"Get: {op[1]} -> {result}")
    # Imprime el estado actual de la caché
    #devuelve lista de elementos clave:valor
    print(f"Estado de la caché: {list(cache.cache.items())}")
