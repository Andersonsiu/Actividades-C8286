import grpc
import analisis_datos_pb2
import analisis_datos_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = analisis_datos_pb2_grpc.AnalisisServiceStub(channel)

        metadata = [('authorization', 'valid_token')]

        try:
            # Prueba del método Agregar
            response = stub.Agregar(analisis_datos_pb2.AgregarRequest(numeros=[1, 2, 3, 4, 5]), metadata=metadata)
            print(f"Resultado de la suma: {response.resultado}")
        except grpc.RpcError as e:
            print(f"Error en la llamada RPC: {e.code()} - {e.details()}")

        try:
            # Prueba del método Filtrar
            response = stub.Filtrar(analisis_datos_pb2.FiltrarRequest(numeros=[1, 2, 3, 4, 5], umbral=3), metadata=metadata)
            print(f"Resultado del filtrado: {response.resultado}")
        except grpc.RpcError as e:
            print(f"Error en la llamada RPC: {e.code()} - {e.details()}")

        try:
            # Prueba del método Transformar
            response = stub.Transformar(analisis_datos_pb2.TransformarRequest(numeros=[1, 2, 3, 4, 5], operacion='doble'), metadata=metadata)
            print(f"Resultado de la transformación (doble): {response.resultado}")
        except grpc.RpcError as e:
            print(f"Error en la llamada RPC: {e.code()} - {e.details()}")

if __name__ == '__main__':
    run()
