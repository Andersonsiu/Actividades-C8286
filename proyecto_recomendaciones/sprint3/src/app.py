from flask import Flask, request, jsonify, Response
from prometheus_client import CollectorRegistry, generate_latest, Counter
from pymongo import MongoClient
import pandas as pd
import traceback
from integracion import Recomendador
import redis
import json

app = Flask(__name__)

# Inicializar el cliente de Prometheus
REQUEST_COUNT = Counter('app_request_count', 'Total Request Count', ['app_name', 'endpoint'])

# Ruta de prueba
@app.route('/test')
def test():
    return "Connection successful"

client = MongoClient('mongodb://mongodb:27017/')
db = client['recomendaciones']

# Configurar Redis
redis_client = redis.Redis(host='redis', port=6379, db=0)

@app.route('/recomendaciones', methods=['POST'])
def obtener_recomendaciones():
    REQUEST_COUNT.labels('flask_app', '/recomendaciones').inc()  # Incrementar el contador de métricas

    data = request.get_json()
    user_id = data['user_id']

    try:
        # Intentar obtener las recomendaciones del caché
        cached_recomendaciones = redis_client.get(f'recomendaciones:{user_id}')
        if cached_recomendaciones:
            response = json.loads(cached_recomendaciones)
            return jsonify(response), 200

        recomendador = Recomendador()
        recomendaciones_usuario = recomendador.recomendar_productos_usuario(user_id)
        recomendaciones_items = recomendador.recomendar_productos_similares(user_id)
        recomendaciones_hibrido = recomendador.recomendar_productos_hibrido(user_id)
        recomendaciones_cluster = recomendador.recomendar_productos_cluster(user_id)

        response = {
            "recomendaciones_usuario": recomendaciones_usuario.to_dict(),
            "recomendaciones_items": recomendaciones_items.to_dict(),
            "recomendaciones_hibrido": recomendaciones_hibrido.to_dict(),
            "recomendaciones_cluster": recomendaciones_cluster.to_dict()
        }

        # Almacenar las recomendaciones en caché con una expiración de 10 minutos (600 segundos)
        redis_client.setex(f'recomendaciones:{user_id}', 600, json.dumps(response))

        return jsonify(response), 200

    except Exception as e:
        print("Error occurred:", str(e))
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

@app.route('/metrics')
def metrics():
    registry = CollectorRegistry()
    registry.register(REQUEST_COUNT)
    return Response(generate_latest(registry), mimetype='text/plain')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

