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

interacciones_df, user_product_matrix = obtener_datos()
if interacciones_df is not None:
    user_id = 'user_1'
    
    # Recomendaciones basadas en clustering
    recomendaciones_cluster = recomendar_productos_cluster(user_id, user_product_matrix)

    # Evaluar el enfoque de clustering
    precision_cluster, recall_cluster, f1_cluster = evaluar_algoritmo(interacciones_df, recomendaciones_cluster)

    # Mejorar la impresión de resultados
    print("Resultados de Evaluación del Clustering:")
    print(f'{"Algoritmo":<20} {"Precisión":<10} {"Recall":<10} {"F1-Score":<10}')
    print(f'{"Cluster-Based":<20} {precision_cluster:<10.2f} {recall_cluster:<10.3f} {f1_cluster:<10.3f}')

    print("\nRecomendaciones Generadas por Clustering:")
    print(f'Recomendaciones Basadas en Clusters: {recomendaciones_cluster.index.tolist()}')

