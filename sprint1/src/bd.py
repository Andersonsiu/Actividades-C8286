from pymongo import MongoClient

def get_database():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['recomendaciones']

    # Crear colecciones si no existen
    if 'usuarios' not in db.list_collection_names():
        db.create_collection('usuarios')
    if 'productos' not in db.list_collection_names():
        db.create_collection('productos')
    if 'interacciones' not in db.list_collection_names():
        db.create_collection('interacciones')

    # Crear índices
    db.usuarios.create_index('email', unique=True)
    db.interacciones.create_index([('user_id', 1), ('producto_id', 1)])
    db.productos.create_index([('nombre', 'text'), ('descripcion', 'text')])

    print("Base de datos y colecciones configuradas con éxito")

    return db
