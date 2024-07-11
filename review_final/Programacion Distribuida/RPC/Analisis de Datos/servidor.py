from concurrent import futures
import grpc
import analisis_datos_pb2
import analisis_datos_pb2_grpc

VALID_TOKENS = ["valid_token"]

class AnalisisService(analisis_datos_pb2_grpc.AnalisisServiceServicer):
    def Agregar(self, request, context):
        if not self.authenticate(context):
            context.abort(grpc.StatusCode.UNAUTHENTICATED, 'Invalid token')
        resultado = sum(request.numeros)
        return analisis_datos_pb2.AgregarResponse(resultado=resultado)

    def Filtrar(self, request, context):
        if not self.authenticate(context):
            context.abort(grpc.StatusCode.UNAUTHENTICATED, 'Invalid token')
        resultado = [num for num in request.numeros if num > request.umbral]
        return analisis_datos_pb2.FiltrarResponse(resultado=resultado)

    def Transformar(self, request, context):
        if not self.authenticate(context):
            context.abort(grpc.StatusCode.UNAUTHENTICATED, 'Invalid token')
        if request.operacion == 'doble':
            resultado = [num * 2 for num in request.numeros]
        elif request.operacion == 'cuadrado':
            resultado = [num ** 2 for num in request.numeros]
        else:
            resultado = request.numeros
        return analisis_datos_pb2.TransformarResponse(resultado=resultado)

    def authenticate(self, context):
        for key, value in context.invocation_metadata():
            if key == 'authorization' and value in VALID_TOKENS:
                return True
        return False

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    analisis_datos_pb2_grpc.add_AnalisisServiceServicer_to_server(AnalisisService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor listo y esperando...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

