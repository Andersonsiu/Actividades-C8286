# cliente.py
import socket

def enviar_mensaje(mensaje):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 65432))  # Conecta al servidor en el puerto 65432
        s.sendall(mensaje.encode())
        data = s.recv(1024)
        print('Mensaje recibido del servidor:', data.decode())

if __name__ == "__main__":
    enviar_mensaje("Hola, servidor")

