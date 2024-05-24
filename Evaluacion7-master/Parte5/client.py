import dill as pickle
import socket
import marshal
import types

def send_job(functions, data, server='127.0.0.1', port=1936):
    conn = socket.create_connection((server, port))
    conn.send(b'\x00')  # Código de operación para enviar trabajo
    serialized_funcs = marshal.dumps(functions.__code__)
    conn.send(len(serialized_funcs).to_bytes(4, 'little'))
    conn.send(serialized_funcs)
    serialized_data = pickle.dumps(data)
    conn.send(len(serialized_data).to_bytes(4, 'little'))
    conn.send(serialized_data)
    job_id = int.from_bytes(conn.recv(4), 'little')
    conn.close()
    return job_id

def get_result(job_id, server='127.0.0.1', port=1936):
    conn = socket.create_connection((server, port))
    conn.send(b'\x01')  # Código de operación para obtener resultados
    conn.send(job_id.to_bytes(4, 'little'))
    result_size = int.from_bytes(conn.recv(4), 'little')
    result = pickle.loads(conn.recv(result_size))
    conn.close()
    return result

def mapper_and_reducer():
    from chunk_mp_mapreduce.test_functions import emitter, mean_reducer
    return emitter, mean_reducer

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    job_id = send_job(mapper_and_reducer, data)
    print(f'Job ID: {job_id}')
    result = get_result(job_id)
    print(f'Result: {result}')
