from pymongo import MongoClient
import pandas as pd

# Conectar a MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['recomendaciones']

# Obtener datos de interacciones
interacciones = db.interacciones.find()
interacciones_df = pd.DataFrame(list(interacciones))

if interacciones_df.empty:
    print("No hay datos de interacciones disponibles.")
else:
    print("Interacciones de entrenamiento:")
    print(interacciones_df.head())

