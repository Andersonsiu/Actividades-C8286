import pandas as pd
from pymongo import MongoClient
from ast import literal_eval

# Conectar a MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['recomendaciones']

# Función para convertir cadena a lista o diccionario
def parse_string(value):
    if pd.isna(value):
        return None
    try:
        return literal_eval(value)
    except (ValueError, SyntaxError):
        return value

# Cargar y insertar usuarios
usuarios_df = pd.read_csv('usuarios.csv')
usuarios_df['preferencias'] = usuarios_df['preferencias'].apply(parse_string)
usuarios_df['historial_compras'] = usuarios_df['historial_compras'].apply(parse_string)
usuarios_df['actividad_navegacion'] = usuarios_df['actividad_navegacion'].apply(parse_string)
usuarios_data = usuarios_df.to_dict(orient='records')
db.usuarios.insert_many(usuarios_data)

# Cargar y insertar productos
productos_df = pd.read_csv('productos.csv')
productos_df['calificaciones'] = productos_df['calificaciones'].apply(parse_string)
productos_df['especificaciones'] = productos_df['especificaciones'].apply(parse_string)
productos_data = productos_df.to_dict(orient='records')
db.productos.insert_many(productos_data)

# Cargar y insertar interacciones
interacciones_df = pd.read_csv('interacciones.csv')
interacciones_df['detalle_interaccion'] = interacciones_df['detalle_interaccion'].apply(parse_string)
interacciones_data = interacciones_df.to_dict(orient='records')
db.interacciones.insert_many(interacciones_data)

print("Datos insertados correctamente")
