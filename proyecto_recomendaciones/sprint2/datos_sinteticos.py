from pymongo import MongoClient
import pandas as pd
import numpy as np
import random
from faker import Faker
import datetime

# Conectar a MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['recomendaciones']

# Generar datos sintéticos
faker = Faker()

# Generar usuarios
usuarios = []
for i in range(100):  # Aumenta el número de usuarios
    usuario = {
        '_id': f'user_{i}',
        'nombre': faker.name(),
        'email': faker.email()
    }
    usuarios.append(usuario)

# Insertar usuarios en la colección
db.usuarios.drop()
db.usuarios.insert_many(usuarios)

# Generar productos
productos = []
for i in range(50):  # Aumenta el número de productos
    producto = {
        '_id': f'producto_{i}',
        'nombre': faker.word(),
        'categoría': random.choice(['tecnología', 'deportes', 'cocina', 'libros', 'ropa']),
        'precio': round(random.uniform(10.0, 500.0), 2),
        'calificaciones': [],
        'disponibilidad': random.choice([True, False]),
        'especificaciones': faker.sentence()
    }
    productos.append(producto)

# Insertar productos en la colección
db.productos.drop()
db.productos.insert_many(productos)

# Generar interacciones
interacciones = []
tipos_interaccion = ['compra', 'click', 'view']
for _ in range(1000):  # Aumenta el número de interacciones
    interaccion = {
        '_id': faker.uuid4(),
        'interaccion_id': faker.uuid4(),
        'user_id': random.choice([usuario['_id'] for usuario in usuarios]),
        'producto_id': random.choice([producto['_id'] for producto in productos]),
        'tipo_interaccion': random.choice(tipos_interaccion),
        'fecha': faker.date_time_this_year(),
        'detalle_interaccion': {}
    }
    interacciones.append(interaccion)

# Insertar interacciones en la colección
db.interacciones.drop()
db.interacciones.insert_many(interacciones)

print("Datos sintéticos generados e insertados en la base de datos.")
