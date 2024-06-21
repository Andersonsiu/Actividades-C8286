from pymongo import MongoClient
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from sklearn.metrics import precision_score, recall_score, f1_score

# Conectar a MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['recomendaciones']

def obtener_datos():
    interacciones = db.interacciones.find()
    interacciones_df = pd.DataFrame(list(interacciones))
    if interacciones_df.empty:
        print("No hay datos disponibles.")
        return None, None
    interacciones_df['tipo_interaccion'] = interacciones_df['tipo_interaccion'].map({'compra': 3, 'click': 1, 'view': 2})
    user_product_matrix = interacciones_df.pivot_table(index='user_id', columns='producto_id', values='tipo_interaccion', fill_value=0)
    return interacciones_df, user_product_matrix

def recomendar_productos_usuario(user_id, user_product_matrix, num_recommendations=5):
    user_similarity = cosine_similarity(user_product_matrix)
    user_similarity_df = pd.DataFrame(user_similarity, index=user_product_matrix.index, columns=user_product_matrix.index)
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

def recomendar_productos_similares(user_id, user_product_matrix, num_recommendations=5):
    item_similarity = cosine_similarity(user_product_matrix.T)
    item_similarity_df = pd.DataFrame(item_similarity, index=user_product_matrix.columns, columns=user_product_matrix.columns)
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

def recomendar_productos_cluster(user_id, user_product_matrix, num_clusters=5, num_recommendations=5):
    kmeans = KMeans(n_clusters=num_clusters)
    clusters = kmeans.fit_predict(user_product_matrix)
    user_clusters = pd.DataFrame({'user_id': user_product_matrix.index, 'cluster': clusters})
    user_cluster = user_clusters[user_clusters['user_id'] == user_id]['cluster'].iloc[0]
    cluster_users = user_clusters[user_clusters['cluster'] == user_cluster]['user_id']
    cluster_interactions = user_product_matrix.loc[cluster_users]
    cluster_recommendations = cluster_interactions.sum().sort_values(ascending=False)
    user_interactions = user_product_matrix.loc[user_id]
    cluster_recommendations = cluster_recommendations[user_interactions == 0]
    cluster_recommendations = cluster_recommendations.head(num_recommendations)
    return cluster_recommendations

def evaluar_algoritmo(interacciones_df, recomendaciones):
    interacciones_df['prediccion'] = interacciones_df.apply(lambda row: 1 if row['producto_id'] in recomendaciones.index else 0, axis=1)
    true_labels = interacciones_df['tipo_interaccion'].apply(lambda x: 1 if x > 0 else 0).values
    pred_labels = interacciones_df['prediccion'].values
    precision = precision_score(true_labels, pred_labels)
    recall = recall_score(true_labels, pred_labels)
    f1 = f1_score(true_labels, pred_labels)
    return precision, recall, f1

def almacenar_recomendaciones(db, user_id, recomendaciones_usuario, recomendaciones_items, recomendaciones_cluster, recomendaciones_hibridas):
    db.recomendaciones_usuario.insert_one({
        'user_id': user_id,
        'recomendaciones_usuario': recomendaciones_usuario.index.tolist(),
        'recomendaciones_items': recomendaciones_items.index.tolist(),
        'recomendaciones_cluster': recomendaciones_cluster.index.tolist(),
        'recomendaciones_hibridas': recomendaciones_hibridas.index.tolist()
    })

interacciones_df, user_product_matrix = obtener_datos()
if interacciones_df is not None:
    user_id = 'user_1'

    # Filtrado colaborativo
    recomendaciones_usuario = recomendar_productos_usuario(user_id, user_product_matrix)
    recomendaciones_items = recomendar_productos_similares(user_id, user_product_matrix)
    
    # Clustering
    recomendaciones_cluster = recomendar_productos_cluster(user_id, user_product_matrix)

    # Recomendaciones híbridas (combinación de recomendaciones basadas en usuarios e ítems)
    recomendaciones_hibridas = pd.concat([recomendaciones_usuario, recomendaciones_items]).groupby(level=0).mean().sort_values(ascending=False).head(5)

    # Evaluar los tres enfoques
    precision_usuario, recall_usuario, f1_usuario = evaluar_algoritmo(interacciones_df, recomendaciones_usuario)
    precision_items, recall_items, f1_items = evaluar_algoritmo(interacciones_df, recomendaciones_items)
    precision_cluster, recall_cluster, f1_cluster = evaluar_algoritmo(interacciones_df, recomendaciones_cluster)
    precision_hibrido, recall_hibrido, f1_hibrido = evaluar_algoritmo(interacciones_df, recomendaciones_hibridas)

    # Impresión de resultados mejorada
    print("Resultados de Evaluación:")
    print(f'{"Algoritmo":<20} {"Precisión":<10} {"Recall":<10} {"F1-Score":<10}')
    print(f'{"User-Based CF":<20} {precision_usuario:<10.2f} {recall_usuario:<10.3f} {f1_usuario:<10.3f}')
    print(f'{"Item-Based CF":<20} {precision_items:<10.2f} {recall_items:<10.3f} {f1_items:<10.3f}')
    print(f'{"Cluster-Based":<20} {precision_cluster:<10.2f} {recall_cluster:<10.3f} {f1_cluster:<10.3f}')
    print(f'{"Híbrido":<20} {precision_hibrido:<10.2f} {recall_hibrido:<10.3f} {f1_hibrido:<10.3f}')

    print("\nRecomendaciones Generadas:")
    print(f'Recomendaciones Basadas en Usuarios: {recomendaciones_usuario.index.tolist()}')
    print(f'Recomendaciones Basadas en Ítems: {recomendaciones_items.index.tolist()}')
    print(f'Recomendaciones Basadas en Clusters: {recomendaciones_cluster.index.tolist()}')
    print(f'Recomendaciones Híbridas: {recomendaciones_hibridas.index.tolist()}')

    # Almacenar recomendaciones
    almacenar_recomendaciones(db, user_id, recomendaciones_usuario, recomendaciones_items, recomendaciones_cluster, recomendaciones_hibridas)

