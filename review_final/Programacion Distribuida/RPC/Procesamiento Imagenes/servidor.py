from concurrent import futures
import grpc
import procesamiento_imagenes_pb2
import procesamiento_imagenes_pb2_grpc
from PIL import Image, ImageFilter
import io

class ProcesamientoImagenesServicer(procesamiento_imagenes_pb2_grpc.ProcesamientoImagenesServicer):
    def validar_usuario(self, context):
        metadata = dict(context.invocation_metadata())
        if 'authorization' not in metadata or metadata['authorization'] != 'valid_token':
            context.abort(grpc.StatusCode.UNAUTHENTICATED, "Token inválido")

    def Filtrar(self, request, context):
        self.validar_usuario(context)
        imagen = Image.open(io.BytesIO(request.imagen))
        if request.operacion == 'blur':
            imagen = imagen.filter(ImageFilter.BLUR)
        elif request.operacion == 'sharpen':
            imagen = imagen.filter(ImageFilter.SHARPEN)
        output = io.BytesIO()
        imagen.save(output, format="JPEG")
        return procesamiento_imagenes_pb2.ImagenResponse(imagen=output.getvalue())

    def Transformar(self, request, context):
        self.validar_usuario(context)
        imagen = Image.open(io.BytesIO(request.imagen))
        if request.operacion == 'rotate':
            imagen = imagen.rotate(90)
        elif request.operacion == 'flip':
            imagen = imagen.transpose(Image.FLIP_LEFT_RIGHT)
        output = io.BytesIO()
        imagen.save(output, format="JPEG")
        return procesamiento_imagenes_pb2.ImagenResponse(imagen=output.getvalue())

    def Analizar(self, request, context):
        self.validar_usuario(context)
        return procesamiento_imagenes_pb2.AnalisisResponse(resultado="Análisis completado")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    procesamiento_imagenes_pb2_grpc.add_ProcesamientoImagenesServicer_to_server(ProcesamientoImagenesServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor listo y esperando...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
