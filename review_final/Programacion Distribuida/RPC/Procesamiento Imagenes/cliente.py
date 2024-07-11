import grpc
import procesamiento_imagenes_pb2
import procesamiento_imagenes_pb2_grpc
from PIL import Image
import io

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = procesamiento_imagenes_pb2_grpc.ProcesamientoImagenesStub(channel)
        
        with open('imagen.jpg', 'rb') as f:
            imagen_bytes = f.read()
        
        # Prueba de filtrado
        response = stub.Filtrar(procesamiento_imagenes_pb2.ImagenRequest(imagen=imagen_bytes, operacion='blur'))
        with open('imagen_filtrada.jpg', 'wb') as f:
            f.write(response.imagen)
        
        # Prueba de transformación
        response = stub.Transformar(procesamiento_imagenes_pb2.ImagenRequest(imagen=imagen_bytes, operacion='rotate'))
        with open('imagen_transformada.jpg', 'wb') as f:
            f.write(response.imagen)
        
        # Prueba de análisis
        response = stub.Analizar(procesamiento_imagenes_pb2.ImagenRequest(imagen=imagen_bytes, operacion='analyze'))
        print(response.resultado)

if __name__ == '__main__':
    run()
