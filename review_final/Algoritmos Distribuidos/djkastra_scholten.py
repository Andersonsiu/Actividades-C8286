class Process:
    def __init__(self, process_id, neighbors):
        self.process_id = process_id  # Identificador del proceso
        self.neighbors = neighbors  # Vecinos del proceso
        self.parent = None  # Padre en el árbol de dependencia
        self.children = set()  # Hijos activos
        self.active = True  # Estado activo

    def send_message(self, recipient):
        print(f"Proceso {self.process_id} envía mensaje a Proceso {recipient.process_id}")
        recipient.receive_message(self, self.process_id)

    def receive_message(self, sender, sender_id):
        print(f"Proceso {self.process_id} recibe mensaje de Proceso {sender_id}")
        if self.parent is None:
            self.parent = sender  # Marca al remitente como padre
        self.children.add(sender_id)  # Agrega al remitente como hijo
        self.process_task()

    def process_task(self):
        print(f"Proceso {self.process_id} está procesando tarea.")
        # Simula el procesamiento de una tarea
        self.active = False  # Marca el proceso como inactivo
        self.check_termination()

    def check_termination(self):
        if not self.active and not self.children:
            print(f"Proceso {self.process_id} verifica terminación.")
            if self.parent:
                self.parent.receive_termination(self.process_id)

    def receive_termination(self, child_id):
        print(f"Proceso {self.process_id} recibe terminación de Proceso {child_id}")
        self.children.remove(child_id)  # Elimina al hijo que ha terminado
        self.check_termination()

# Ejemplo de uso
processes = [Process(i, []) for i in range(5)]
for process in processes:
    process.neighbors = [p for p in processes if p != process]

# Iniciar la detección de terminación
initiator = processes[0]
initiator.send_message(processes[1])
