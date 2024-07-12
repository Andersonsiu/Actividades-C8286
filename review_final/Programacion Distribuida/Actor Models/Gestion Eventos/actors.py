# actors.py
import pykka

class EventActor(pykka.ThreadingActor):
    def __init__(self, event_type):
        super().__init__()
        self.event_type = event_type

    def on_receive(self, message):
        print(f"Evento recibido en {self.event_type}: {message}")

class UserEventActor(EventActor):
    def __init__(self):
        super().__init__('user_event')

    def on_receive(self, message):
        super().on_receive(message)
        print("Procesando evento de usuario...")

class SystemEventActor(EventActor):
    def __init__(self):
        super().__init__('system_event')

    def on_receive(self, message):
        super().on_receive(message)
        print("Procesando evento del sistema...")

class RouterActor(pykka.ThreadingActor):
    def __init__(self):
        super().__init__()
        self.actors = {
            'user_event': UserEventActor.start(),
            'system_event': SystemEventActor.start()
        }

    def on_receive(self, message):
        event_type = message.get('type')
        if event_type in self.actors:
            self.actors[event_type].tell(message)
        else:
            print(f"No se encontró un actor para el tipo de evento: {event_type}")

class SupervisorActor(pykka.ThreadingActor):
    def __init__(self):
        super().__init__()
        self.router = RouterActor.start()

    def on_receive(self, message):
        self.router.tell(message)
