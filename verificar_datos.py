from pymongo import MongoClient

# Conectar a MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['recomendaciones']

# Verificar datos de usuarios
print("Usuarios:")
for user in db.usuarios.find().limit(5):
    print(user)

# Verificar datos de productos
print("\nProductos:")
for product in db.productos.find().limit(5):
    print(product)

# Verificar datos de interacciones
print("\nInteracciones:")
for interaction in db.interacciones.find().limit(5):
    print(interaction)
