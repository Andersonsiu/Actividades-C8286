from pymongo import MongoClient

# Conectar a MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['recomendaciones']

# Crear colecciones
db.create_collection('usuarios')
db.create_collection('productos')
db.create_collection('interacciones')

# Crear índices
db.usuarios.create_index('email', unique=True)
db.interacciones.create_index([('user_id', 1), ('producto_id', 1)])
db.productos.create_index([('nombre', 'text'), ('descripcion', 'text')])

print("Base de datos y colecciones creadas con éxito")
