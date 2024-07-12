# send_event.py
import zmq
import threading

def send_event(event_type, data):
    context = zmq.Context()
    socket = context.socket(zmq.PUSH)
    socket.connect("tcp://localhost:5555")
    event = {'type': event_type, 'data': data}
    socket.send_json(event)

# Ejemplo de enviar eventos
if __name__ == "__main__":
    threading.Thread(target=send_event, args=('user_event', {'user_id': 1, 'action': 'login'})).start()
    threading.Thread(target=send_event, args=('system_event', {'status': 'ok'})).start()
