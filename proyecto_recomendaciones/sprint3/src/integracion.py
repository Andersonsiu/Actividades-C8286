# integracion.py
from pymongo import MongoClient
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from sklearn.cluster import KMeans

class Recomendador:
    def __init__(self):
        # Conectar a MongoDB
        self.client = MongoClient('mongodb://mongodb:27017/')
        self.db = self.client['recomendaciones']

        # Obtener datos de interacciones
        interacciones = self.db.interacciones.find()
        self.interacciones_df = pd.DataFrame(list(interacciones))

        # Mapear tipo_interaccion a valores numéricos
        self.interacciones_df['tipo_interaccion'] = self.interacciones_df['tipo_interaccion'].map({'compra': 3, 'click': 1, 'view': 2})

        # Dividir los datos en conjuntos de entrenamiento y prueba
        self.train_df, self.test_df = train_test_split(self.interacciones_df, test_size=0.2, random_state=42)

        # Crear una matriz de usuario-producto para el conjunto de entrenamiento
        self.user_product_matrix_train = self.train_df.pivot_table(index='user_id', columns='producto_id', values='tipo_interaccion', fill_value=0)

        # Calcular la similitud del coseno entre los usuarios
        self.user_similarity = cosine_similarity(self.user_product_matrix_train)
        self.user_similarity_df = pd.DataFrame(self.user_similarity, index=self.user_product_matrix_train.index, columns=self.user_product_matrix_train.index)

        # Calcular la similitud del coseno entre los productos
        self.item_similarity = cosine_similarity(self.user_product_matrix_train.T)
        self.item_similarity_df = pd.DataFrame(self.item_similarity, index=self.user_product_matrix_train.columns, columns=self.user_product_matrix_train.columns)

    def recomendar_productos_usuario(self, user_id, num_recommendations=30, top_n_similar_users=100):
        if user_id not in self.user_similarity_df.columns:
            return pd.Series(dtype='float64')

        similar_users = self.user_similarity_df[user_id].sort_values(ascending=False).head(top_n_similar_users)
        user_interactions = self.user_product_matrix_train.loc[user_id]
        recommendations = pd.Series(dtype='float64')

        for similar_user, similarity in similar_users.items():
            if similar_user != user_id:
                similar_user_interactions = self.user_product_matrix_train.loc[similar_user]
                recommendations = pd.concat([recommendations, similar_user_interactions[similar_user_interactions > 0] * similarity])

        recommendations = recommendations.groupby(recommendations.index).sum()
        recommendations = recommendations[user_interactions == 0]
        recommendations = recommendations.sort_values(ascending=False).head(num_recommendations)

        return recommendations

    def recomendar_productos_similares(self, user_id, num_recommendations=30, top_n_similar_items=100):
        user_interactions = self.user_product_matrix_train.loc[user_id]
        similar_items = pd.Series(dtype='float64')

        for product, interaction in user_interactions.items():
            if interaction > 0:
                similar_products = self.item_similarity_df[product].sort_values(ascending=False).head(top_n_similar_items)
                similar_items = pd.concat([similar_items, similar_products * interaction])

        similar_items = similar_items.groupby(similar_items.index).sum()
        similar_items = similar_items[user_interactions == 0]
        similar_items = similar_items.sort_values(ascending=False).head(num_recommendations)

        return similar_items

    def recomendar_productos_hibrido(self, user_id, num_recommendations=30, weight_user=0.7, weight_item=0.3):
        recomendaciones_usuario = self.recomendar_productos_usuario(user_id, num_recommendations)
        recomendaciones_items = self.recomendar_productos_similares(user_id, num_recommendations)

        recomendaciones_combinadas = pd.concat([
            recomendaciones_usuario * weight_user,
            recomendaciones_items * weight_item
        ])

        recomendaciones_combinadas = recomendaciones_combinadas.groupby(recomendaciones_combinadas.index).sum()
        recomendaciones_combinadas = recomendaciones_combinadas.sort_values(ascending=False).head(num_recommendations)

        return recomendaciones_combinadas

    def recomendar_productos_cluster(self, user_id, num_clusters=5, num_recommendations=30):
        kmeans = KMeans(n_clusters=num_clusters, random_state=42)
        clusters = kmeans.fit_predict(self.user_product_matrix_train)
        user_clusters = pd.DataFrame({'user_id': self.user_product_matrix_train.index, 'cluster': clusters})

        if user_id not in user_clusters['user_id'].values:
            return pd.Series(dtype='float64')

        user_cluster = user_clusters[user_clusters['user_id'] == user_id]['cluster'].iloc[0]
        cluster_users = user_clusters[user_clusters['cluster'] == user_cluster]['user_id']
        cluster_interactions = self.user_product_matrix_train.loc[cluster_users]
        cluster_recommendations = cluster_interactions.sum().sort_values(ascending=False)
        user_interactions = self.user_product_matrix_train.loc[user_id]
        cluster_recommendations = cluster_recommendations[user_interactions == 0]
        cluster_recommendations = cluster_recommendations.head(num_recommendations)
        return cluster_recommendations

    def evaluar_algoritmo(self, test_df, recomendaciones, threshold=1):
        test_df['prediccion'] = test_df.apply(lambda row: 1 if row['producto_id'] in recomendaciones.index else 0, axis=1)
        true_labels = test_df['tipo_interaccion'].apply(lambda x: 1 if x >= threshold else 0).values
        pred_labels = test_df['prediccion'].values
        precision = precision_score(true_labels, pred_labels, zero_division=1)
        recall = recall_score(true_labels, pred_labels, zero_division=1)
        f1 = f1_score(true_labels, pred_labels, zero_division=1)
        return precision, recall, f1

    def calcular_y_almacenar_recomendaciones(self, user_ids):
        with ProcessPoolExecutor() as executor:
            resultados = list(executor.map(self.calcular_recomendaciones, user_ids))

        with ThreadPoolExecutor() as executor:
            resultados_cluster = list(executor.map(self.recomendar_productos_cluster, user_ids, [self.user_product_matrix_train]*len(user_ids)))

        recomendaciones = []

        for user_id, (rec_user, rec_item, rec_hib), rec_cluster in zip(user_ids, resultados, resultados_cluster):
            recomendaciones.append({
                'user_id': user_id,
                'recomendaciones_usuario': rec_user.to_dict(),
                'recomendaciones_items': rec_item.to_dict(),
                'recomendaciones_hibrido': rec_hib.to_dict(),
                'recomendaciones_cluster': rec_cluster.to_dict()
            })

        self.db.recomendaciones_totales.insert_many(recomendaciones)

    def calcular_recomendaciones(self, user_id):
        recomendaciones_usuario = self.recomendar_productos_usuario(user_id)
        recomendaciones_items = self.recomendar_productos_similares(user_id)
        recomendaciones_hibrido = self.recomendar_productos_hibrido(user_id)
        return recomendaciones_usuario, recomendaciones_items, recomendaciones_hibrido

    def imprimir_recomendaciones(self, user_id):
        recomendaciones_usuario, recomendaciones_items, recomendaciones_hibrido = self.calcular_recomendaciones(user_id)
        recomendaciones_cluster = self.recomendar_productos_cluster(user_id)

        precision_usuario, recall_usuario, f1_usuario = self.evaluar_algoritmo(self.test_df, recomendaciones_usuario)
        precision_items, recall_items, f1_items = self.evaluar_algoritmo(self.test_df, recomendaciones_items)
        precision_hibrido, recall_hibrido, f1_hibrido = self.evaluar_algoritmo(self.test_df, recomendaciones_hibrido)
        precision_cluster, recall_cluster, f1_cluster = self.evaluar_algoritmo(self.test_df, recomendaciones_cluster)

        print("\nResultados de Recomendaciones Basadas en Filtrado Colaborativo:\n")
        print("Recomendaciones basadas en usuarios:")
        print(recomendaciones_usuario)

        print("\nRecomendaciones basadas en ítems:")
        print(recomendaciones_items)

        print("\nRecomendaciones híbridas:")
        print(recomendaciones_hibrido)

        print("\nRecomendaciones basadas en clustering:")
        print(recomendaciones_cluster)

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

        print("\nResultados de Evaluación de Recomendaciones Basadas en Clustering:\n")
        print(f'{"Métrica":<15} {"Valor":<10}')
        print(f'{"Precisión":<15} {precision_cluster:<10.2f}')
        print(f'{"Recall":<15} {recall_cluster:<10.3f}')
        print(f'{"F1-Score":<15} {f1_cluster:<10.3f}')

# Inicialización y cálculo de recomendaciones
if __name__ == "__main__":
    recomendador = Recomendador()
    user_ids = recomendador.interacciones_df['user_id'].unique()
    recomendador.calcular_y_almacenar_recomendaciones(user_ids)
    recomendador.imprimir_recomendaciones('user_1')

