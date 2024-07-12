import threading
import queue

# Algoritmo de Dijkstra-Scholten

class Process:
    def __init__(self, process_id):
        self.process_id = process_id
        self.parent = None
        self.children = set()
        self.active = True

    def send_message(self, recipient):
        recipient.receive_message(self, self.process_id)

    def receive_message(self, sender, sender_id):
        if self.parent is None:
            self.parent = sender
        self.children.add(sender_id)
        self.process_task()

    def process_task(self):
        self.active = False
        self.check_termination()

    def check_termination(self):
        if not self.active and not self.children:
            if self.parent:
                self.parent.receive_termination(self.process_id)

    def receive_termination(self, child_id):
        self.children.remove(child_id)
        self.check_termination()

# Algoritmo de Ricart-Agrawala

class RicartAgrawalaNode:
    def __init__(self, node_id, num_nodes):
        self.node_id = node_id
        self.num_nodes = num_nodes
        self.clock = 0
        self.request_queue = []
        self.replies_received = 0

    def request_access(self):
        self.clock += 1
        self.request_queue.append((self.clock, self.node_id))
        for node in nodes:
            if node.node_id != self.node_id:
                node.receive_request(self.clock, self.node_id)

    def receive_request(self, timestamp, sender_id):
        self.clock = max(self.clock, timestamp) + 1
        self.request_queue.append((timestamp, sender_id))
        self.request_queue.sort()
        self.send_reply(sender_id)

    def send_reply(self, target_id):
        for node in nodes:
            if node.node_id == target_id:
                node.receive_reply(self.node_id)

    def receive_reply(self, sender_id):
        self.replies_received += 1
        if self.replies_received == self.num_nodes - 1:
            self.enter_critical_section()

    def enter_critical_section(self):
        print(f"Node {self.node_id} entering critical section")
        self.leave_critical_section()

    def leave_critical_section(self):
        self.replies_received = 0
        self.request_queue = [(t, n) for t, n in self.request_queue if n != self.node_id]
        for timestamp, node_id in self.request_queue:
            self.send_reply(node_id)
        print(f"Node {self.node_id} leaving critical section")

if __name__ == "__main__":
    # Ejecutar Dijkstra-Scholten
    print("Ejecutando Dijkstra-Scholten:")
    dijkstra_processes = [Process(i) for i in range(5)]
    dijkstra_processes[0].send_message(dijkstra_processes[1])
    print()

    # Ejecutar Ricart-Agrawala
    print("Ejecutando Ricart-Agrawala:")
    nodes = [RicartAgrawalaNode(i, 3) for i in range(3)]
    nodes[0].request_access()
