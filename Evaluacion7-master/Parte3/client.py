import dill as pickle
import socket
from time import sleep

def send_map_reduce_request(data):
    conn = None
    try:
        conn = socket.create_connection(('127.0.0.1', 1936))
        conn.send(b'\x05')  # Código de operación para map-reduce
        data_bytes = pickle.dumps(data)
        conn.send(len(data_bytes).to_bytes(4, 'little'))
        conn.send(data_bytes)
        job_id = int.from_bytes(conn.recv(4), 'little')
        print(f'Obteniendo datos desde job_id {job_id}')
    finally:
        if conn:
            conn.close()

    result = None
    while result is None:
        try:
            conn = socket.create_connection(('127.0.0.1', 1936))
            conn.send(b'\x01')
            conn.send(job_id.to_bytes(4, 'little'))
            result_size = int.from_bytes(conn.recv(4), 'little')
            result = pickle.loads(conn.recv(result_size))
        finally:
            if conn:
                conn.close()
        sleep(1)
    print(f'El resultado de la operación map-reduce es {result}')

if __name__ == '__main__':
    words = 'Python es lo mejor Python rocks'.split(' ')
    send_map_reduce_request(words)
