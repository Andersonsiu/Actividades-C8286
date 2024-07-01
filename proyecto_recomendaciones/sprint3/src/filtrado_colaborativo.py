from pymongo import MongoClient
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from concurrent.futures import ProcessPoolExecutor

# Conectar a MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['recomendaciones']

# Obtener datos de interacciones
interacciones = db.interacciones.find()
interacciones_df = pd.DataFrame(list(interacciones))

# Mapear tipo_interaccion a valores numéricos
interacciones_df['tipo_interaccion'] = interacciones_df['tipo_interaccion'].map({'compra': 3, 'click': 1, 'view': 2})

# Dividir los datos en conjuntos de entrenamiento y prueba
train_df, test_df = train_test_split(interacciones_df, test_size=0.2, random_state=42)

# Crear una matriz de usuario-producto para el conjunto de entrenamiento
user_product_matrix_train = train_df.pivot_table(index='user_id', columns='producto_id', values='tipo_interaccion', fill_value=0)

# Calcular la similitud del coseno entre los usuarios
user_similarity = cosine_similarity(user_product_matrix_train)
user_similarity_df = pd.DataFrame(user_similarity, index=user_product_matrix_train.index, columns=user_product_matrix_train.index)

# Calcular la similitud del coseno entre los productos
item_similarity = cosine_similarity(user_product_matrix_train.T)
item_similarity_df = pd.DataFrame(item_similarity, index=user_product_matrix_train.columns, columns=user_product_matrix_train.columns)

# Función para recomendar productos a un usuario basado en la similitud con otros usuarios
def recomendar_productos_usuario(user_id, num_recommendations=30, top_n_similar_users=100):
    if user_id not in user_similarity_df.columns:
        return pd.Series(dtype='float64')

    similar_users = user_similarity_df[user_id].sort_values(ascending=False).head(top_n_similar_users)
    user_interactions = user_product_matrix_train.loc[user_id]
    recommendations = pd.Series(dtype='float64')

    for similar_user, similarity in similar_users.items():
        if similar_user != user_id:
            similar_user_interactions = user_product_matrix_train.loc[similar_user]
            recommendations = pd.concat([recommendations, similar_user_interactions[similar_user_interactions > 0] * similarity])

    recommendations = recommendations.groupby(recommendations.index).sum()
    recommendations = recommendations[user_interactions == 0]
    recommendations = recommendations.sort_values(ascending=False).head(num_recommendations)

    return recommendations

# Función para recomendar productos similares a los que el usuario ya ha consumido
def recomendar_productos_similares(user_id, num_recommendations=30, top_n_similar_items=100):
    user_interactions = user_product_matrix_train.loc[user_id]
    similar_items = pd.Series(dtype='float64')

    for product, interaction in user_interactions.items():
        if interaction > 0:
            similar_products = item_similarity_df[product].sort_values(ascending=False).head(top_n_similar_items)
            similar_items = pd.concat([similar_items, similar_products * interaction])

    similar_items = similar_items.groupby(similar_items.index).sum()
    similar_items = similar_items[user_interactions == 0]
    similar_items = similar_items.sort_values(ascending=False).head(num_recommendations)

    return similar_items

# Función híbrida para combinar recomendaciones de usuarios e ítems
def recomendar_productos_hibrido(user_id, num_recommendations=30, weight_user=0.7, weight_item=0.3):
    recomendaciones_usuario = recomendar_productos_usuario(user_id, num_recommendations)
    recomendaciones_items = recomendar_productos_similares(user_id, num_recommendations)
    
    recomendaciones_combinadas = pd.concat([
        recomendaciones_usuario * weight_user, 
        recomendaciones_items * weight_item
    ])
    
    recomendaciones_combinadas = recomendaciones_combinadas.groupby(recomendaciones_combinadas.index).sum()
    recomendaciones_combinadas = recomendaciones_combinadas.sort_values(ascending=False).head(num_recommendations)
    
    return recomendaciones_combinadas

# Función para calcular recomendaciones en paralelo
def calcular_recomendaciones(user_id):
    recomendaciones_usuario = recomendar_productos_usuario(user_id)
    recomendaciones_items = recomendar_productos_similares(user_id)
    recomendaciones_hibrido = recomendar_productos_hibrido(user_id)
    return recomendaciones_usuario, recomendaciones_items, recomendaciones_hibrido

# Ejemplo de uso
user_id = 'user_1'

with ProcessPoolExecutor() as executor:
    futuros = executor.submit(calcular_recomendaciones, user_id)
    recomendaciones_usuario, recomendaciones_items, recomendaciones_hibrido = futuros.result()

# Evaluación de las recomendaciones
def evaluar_algoritmo(test_df, recomendaciones, threshold=1):
    test_df['prediccion'] = test_df.apply(lambda row: 1 if row['producto_id'] in recomendaciones.index else 0, axis=1)
    true_labels = test_df['tipo_interaccion'].apply(lambda x: 1 if x >= threshold else 0).values
    pred_labels = test_df['prediccion'].values
    precision = precision_score(true_labels, pred_labels, zero_division=1)
    recall = recall_score(true_labels, pred_labels, zero_division=1)
    f1 = f1_score(true_labels, pred_labels, zero_division=1)
    return precision, recall, f1

precision_usuario, recall_usuario, f1_usuario = evaluar_algoritmo(test_df, recomendaciones_usuario)
precision_items, recall_items, f1_items = evaluar_algoritmo(test_df, recomendaciones_items)
precision_hibrido, recall_hibrido, f1_hibrido = evaluar_algoritmo(test_df, recomendaciones_hibrido)

# Mejorar la impresión de resultados
def imprimir_recomendaciones():
    print("\nResultados de Recomendaciones Basadas en Filtrado Colaborativo:\n")
    print("Recomendaciones basadas en usuarios:")
    print(recomendaciones_usuario)
    
    print("\nRecomendaciones basadas en ítems:")
    print(recomendaciones_items)
    
    print("\nRecomendaciones híbridas:")
    print(recomendaciones_hibrido)
  
    print("\nResultados de Evaluación de Recomendaciones Basadas en Usuarios:\n")
    print(f'{"Métrica":<15} {"Valor":<10}')
    print(f'{"Precisión":<15} {precision_usuario:<10.2f}')
    print(f'{"Recall":<15} {recall_usuario:<10.3f}')
    print(f'{"F1-Score":<15} {f1_usuario:<10.3f}')
    
    print("\nResultados de Evaluación de Recomendaciones Basadas en Ítems:\n")
    print(f'{"Métrica":<15} {"Valor":<10}')
    print(f'{"Precisión":<15} {precision_items:<10.2f}')
    print(f'{"Recall":<15} {recall_items:<10.3f}')
    print(f'{"F1-Score":<15} {f1_items:<10.3f}')
    
    print("\nResultados de Evaluación de Recomendaciones Híbridas:\n")
    print(f'{"Métrica":<15} {"Valor":<10}')
    print(f'{"Precisión":<15} {precision_hibrido:<10.2f}')
    print(f'{"Recall":<15} {recall_hibrido:<10.3f}')
    print(f'{"F1-Score":<15} {f1_hibrido:<10.3f}')

# Llamar a la función de impresión
imprimir_recomendaciones()

