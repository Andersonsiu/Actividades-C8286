import numpy as np
from concurrent.futures import ThreadPoolExecutor

def initialize_centroids(data, k):
    indices = np.random.choice(data.shape[0], k, replace=False)
    return data[indices]

def assign_clusters(data, centroids):
    clusters = {}
    for x in data:
        closest_centroid = np.argmin([np.linalg.norm(x - centroid) for centroid in centroids])
        if closest_centroid not in clusters:
            clusters[closest_centroid] = []
        clusters[closest_centroid].append(x)
    return clusters

def update_centroids(clusters):
    return [np.mean(clusters[k], axis=0) for k in clusters]

def kmeans_parallel(data, k, num_workers=4, max_iters=100):
    centroids = initialize_centroids(data, k)
    for _ in range(max_iters):
        with ThreadPoolExecutor(max_workers=num_workers) as executor:
            clusters = list(executor.map(lambda c: assign_clusters(data, c), [centroids]))[0]
        centroids = update_centroids(clusters)
    return centroids, clusters

if __name__ == "__main__":
    data = np.random.rand(1000, 2)  # Datos de ejemplo
    k = 3
    centroids, clusters = kmeans_parallel(data, k)
    print("Centroides:", centroids)
    print("Clusters:", clusters)
