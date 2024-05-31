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

def send_distributed_map_reduce_request(data):
    conn = None
    try:
        conn = socket.create_connection(('127.0.0.1', 1936))
        conn.send(b'\x06')  # Código de operación para map-reduce distribuido
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
    print(f'El resultado de la operación map-reduce distribuido es {result}')

def send_load_balanced_map_reduce_request(data):
    conn = None
    try:
        conn = socket.create_connection(('127.0.0.1', 1936))
        conn.send(b'\x07')  # Código de operación para map-reduce con balanceo de carga
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
    print(f'El resultado de la operación map-reduce con balanceo de carga es {result}')

def send_fault_tolerant_map_reduce_request(data):
    conn = None
    try:
        conn = socket.create_connection(('127.0.0.1', 1936))
        conn.send(b'\x08')  # Código de operación para map-reduce con tolerancia a fallos
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
    print(f'El resultado de la operación map-reduce con tolerancia a fallos es {result}')

def send_optimized_map_reduce_request(data):
    conn = None
    try:
        conn = socket.create_connection(('127.0.0.1', 1936))
        conn.send(b'\x09')  # Código de operación para map-reduce optimizado
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
    print(f'El resultado de la operación map-reduce optimizado es {result}')

if __name__ == '__main__':
    words = 'Python es lo mejor Python rocks'.split(' ')
    # Elige una de las funciones para probar
    send_map_reduce_request(words)
    # send_distributed_map_reduce_request(words)
    # send_load_balanced_map_reduce_request(words)
    # send_fault_tolerant_map_reduce_request(words)
    # send_optimized_map_reduce_request(words)
