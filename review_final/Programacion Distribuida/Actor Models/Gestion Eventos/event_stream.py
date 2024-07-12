# event_stream.py
import pykka
import zmq

class EventStreamActor(pykka.ThreadingActor):
    def __init__(self, supervisor):
        super().__init__()
        self.supervisor = supervisor
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PULL)
        self.socket.bind("tcp://*:5555")

    def on_start(self):
        while True:
            message = self.socket.recv_json()
            self.supervisor.tell(message)
