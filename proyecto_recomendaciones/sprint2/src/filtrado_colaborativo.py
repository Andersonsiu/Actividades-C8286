from pymongo import MongoClient
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import precision_score, recall_score, f1_score

# Conectar a MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['recomendaciones']

# Obtener datos de interacciones
interacciones = db.interacciones.find()
interacciones_df = pd.DataFrame(list(interacciones))

# Mapear tipo_interaccion a valores numéricos
interacciones_df['tipo_interaccion'] = interacciones_df['tipo_interaccion'].map({'compra': 3, 'click': 1, 'view': 2})

# Crear una matriz de usuario-producto
user_product_matrix = interacciones_df.pivot_table(index='user_id', columns='producto_id', values='tipo_interaccion', fill_value=0)

# Calcular la similitud del coseno entre los usuarios
user_similarity = cosine_similarity(user_product_matrix)
user_similarity_df = pd.DataFrame(user_similarity, index=user_product_matrix.index, columns=user_product_matrix.index)

# Calcular la similitud del coseno entre los productos
item_similarity = cosine_similarity(user_product_matrix.T)
item_similarity_df = pd.DataFrame(item_similarity, index=user_product_matrix.columns, columns=user_product_matrix.columns)

# Función para recomendar productos a un usuario basado en la similitud con otros usuarios
def recomendar_productos_usuario(user_id, num_recommendations=5):
    if user_id not in user_similarity_df.columns:
        return pd.Series(dtype='float64')

    similar_users = user_similarity_df[user_id].sort_values(ascending=False)
    user_interactions = user_product_matrix.loc[user_id]
    recommendations = pd.Series(dtype='float64')

    for similar_user, similarity in similar_users.items():
        if similar_user != user_id:
            similar_user_interactions = user_product_matrix.loc[similar_user]
            recommendations = pd.concat([recommendations, similar_user_interactions[similar_user_interactions > 0]])

    recommendations = recommendations.groupby(recommendations.index).sum()
    recommendations = recommendations[user_interactions == 0]
    recommendations = recommendations.sort_values(ascending=False).head(num_recommendations)

    return recommendations

# Función para recomendar productos similares a los que el usuario ya ha consumido
def recomendar_productos_similares(user_id, num_recommendations=5):
    user_interactions = user_product_matrix.loc[user_id]
    similar_items = pd.Series(dtype='float64')

    for product, interaction in user_interactions.items():
        if interaction > 0:
            similar_products = item_similarity_df[product].sort_values(ascending=False)
            similar_items = pd.concat([similar_items, similar_products])

    similar_items = similar_items.groupby(similar_items.index).sum()
    similar_items = similar_items[user_interactions == 0]
    similar_items = similar_items.sort_values(ascending=False).head(num_recommendations)

    return similar_items

# Ejemplo de uso
user_id = 'user_1'
recomendaciones_usuario = recomendar_productos_usuario(user_id)
recomendaciones_items = recomendar_productos_similares(user_id)

# Evaluación de las recomendaciones
def evaluar_algoritmo(interacciones_df, recomendaciones):
    interacciones_df['prediccion'] = interacciones_df.apply(lambda row: 1 if row['producto_id'] in recomendaciones.index else 0, axis=1)
    true_labels = interacciones_df['tipo_interaccion'].apply(lambda x: 1 if x > 0 else 0).values
    pred_labels = interacciones_df['prediccion'].values
    precision = precision_score(true_labels, pred_labels)
    recall = recall_score(true_labels, pred_labels)
    f1 = f1_score(true_labels, pred_labels)
    return precision, recall, f1

precision_usuario, recall_usuario, f1_usuario = evaluar_algoritmo(interacciones_df, recomendaciones_usuario)
precision_items, recall_items, f1_items = evaluar_algoritmo(interacciones_df, recomendaciones_items)

# Mejorar la impresión de resultados
def imprimir_recomendaciones():
    print("\nResultados de Recomendaciones Basadas en Filtrado Colaborativo:\n")
    print("Recomendaciones basadas en usuarios:")
    print(recomendaciones_usuario)
    
    print("\nRecomendaciones basadas en ítems:")
    print(recomendaciones_items)
  
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

# Llamar a la función de impresión
imprimir_recomendaciones()

