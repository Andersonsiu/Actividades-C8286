from pymongo import MongoClient
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from concurrent.futures import ProcessPoolExecutor

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

def recomendar_productos_cluster(user_id, user_product_matrix, num_clusters=50, num_recommendations=100):
    scaler = StandardScaler()
    user_product_matrix_scaled = scaler.fit_transform(user_product_matrix)
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    clusters = kmeans.fit_predict(user_product_matrix_scaled)
    user_clusters = pd.DataFrame({'user_id': user_product_matrix.index, 'cluster': clusters})
    
    if user_id not in user_clusters['user_id'].values:
        print(f"El usuario {user_id} no se encuentra en la base de datos.")
        return pd.Series(dtype='float64')
    
    user_cluster = user_clusters[user_clusters['user_id'] == user_id]['cluster'].iloc[0]
    cluster_users = user_clusters[user_clusters['cluster'] == user_cluster]['user_id']
    cluster_interactions = user_product_matrix.loc[cluster_users]
    
    # Recomendaciones basadas en el cluster
    cluster_recommendations = cluster_interactions.sum().sort_values(ascending=False)
    user_interactions = user_product_matrix.loc[user_id]
    cluster_recommendations = cluster_recommendations[user_interactions == 0]
    
    # Incluir recomendaciones de usuarios similares dentro del cluster
    user_similarity = cosine_similarity(user_product_matrix.loc[cluster_users])
    user_similarity_df = pd.DataFrame(user_similarity, index=cluster_users, columns=cluster_users)
    
    similar_users = user_similarity_df[user_id].sort_values(ascending=False).index
    similar_user_recommendations = pd.Series(dtype='float64')

    for similar_user in similar_users:
        if similar_user != user_id:
            similar_user_interactions = user_product_matrix.loc[similar_user]
            similar_user_recommendations = pd.concat([similar_user_recommendations, similar_user_interactions[similar_user_interactions > 0]])
    
    similar_user_recommendations = similar_user_recommendations.groupby(similar_user_recommendations.index).sum()
    similar_user_recommendations = similar_user_recommendations[user_interactions == 0]
    
    # Combinar recomendaciones del cluster y de usuarios similares
    combined_recommendations = pd.concat([cluster_recommendations, similar_user_recommendations]).groupby(level=0).sum()
    combined_recommendations = combined_recommendations.sort_values(ascending=False).head(num_recommendations)
    
    return combined_recommendations

def evaluar_algoritmo(test_df, recomendaciones, threshold=1):
    test_df['prediccion'] = test_df.apply(lambda row: 1 if row['producto_id'] in recomendaciones.index else 0, axis=1)
    true_labels = test_df['tipo_interaccion'].apply(lambda x: 1 if x >= threshold else 0).values
    pred_labels = test_df['prediccion'].values
    precision = precision_score(true_labels, pred_labels, zero_division=1)
    recall = recall_score(true_labels, pred_labels, zero_division=1)
    f1 = f1_score(true_labels, pred_labels, zero_division=1)
    return precision, recall, f1

def procesar_usuario(user_id, train_matrix, test_df, num_clusters, num_recommendations):
    recomendaciones = recomendar_productos_cluster(user_id, train_matrix, num_clusters=num_clusters, num_recommendations=num_recommendations)
    precision, recall, f1 = evaluar_algoritmo(test_df, recomendaciones)
    return user_id, recomendaciones, precision, recall, f1

# Obtener datos
interacciones_df, user_product_matrix = obtener_datos()

if interacciones_df is not None:
    # Dividir los datos en conjuntos de entrenamiento y prueba
    train_df, test_df = train_test_split(interacciones_df, test_size=0.2, random_state=42)
    train_matrix = train_df.pivot_table(index='user_id', columns='producto_id', values='tipo_interaccion', fill_value=0)

    user_id = 'user_1'
    num_clusters = 50
    num_recommendations = 100  # Aumentar el número de recomendaciones

    # Usar ProcessPoolExecutor para concurrencia
    with ProcessPoolExecutor() as executor:
        resultado = executor.submit(procesar_usuario, user_id, train_matrix, test_df, num_clusters, num_recommendations).result()

    # Mejorar la impresión de resultados
    user_id, recomendaciones, precision, recall, f1 = resultado
    print(f"\nResultados de Recomendaciones Basadas en Clustering para usuario {user_id}:\n")
    print("Recomendaciones basadas en clustering:")
    print(recomendaciones)
    
    print("\nResultados de Evaluación de Recomendaciones Basadas en Clustering:\n")
    print(f'{"Métrica":<15} {"Valor":<10}')
    print(f'{"Precisión":<15} {precision:<10.2f}')
    print(f'{"Recall":<15} {recall:<10.3f}')
    print(f'{"F1-Score":<15} {f1:<10.3f}')

