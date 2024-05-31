# -*- coding: utf-8 -*-
# servidor.py
import socket

def iniciar_servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', 65432))  # El servidor escucha en el puerto 65432
        s.listen()
        print("Servidor esperando conexion...")
        conn, addr = s.accept()
        with conn:
            print('Conectado por', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print('Mensaje recibido:', data.decode())
                conn.sendall(data)

if __name__ == "__main__":
    iniciar_servidor()

