import threading
import random
import time
from datetime import datetime, timedelta

# Tolerancia a Fallos Bizantina (Simplificado)

class ByzantineNode:
    def __init__(self, node_id, is_faulty=False):
        self.node_id = node_id
        self.is_faulty = is_faulty
        self.state = random.choice(["correct", "faulty"]) if is_faulty else "correct"

    def broadcast_state(self, nodes):
        for node in nodes:
            if node != self:
                node.receive_state(self.node_id, self.state)

    def receive_state(self, sender_id, state):
        print(f"Node {self.node_id} received state '{state}' from Node {sender_id}")

def simulate_byzantine(nodes):
    for node in nodes:
        node.broadcast_state(nodes)

# Algoritmo de Cristian

class CristianNode:
    def __init__(self, node_id, offset):
        self.node_id = node_id
        self.clock = datetime.now() + offset

    def synchronize_time(self, server_time):
        self.clock = server_time

def cristian_algorithm(nodes, server_time):
    for node in nodes:
        node.synchronize_time(server_time)
        print(f"Node {node.node_id} synchronized clock: {node.clock}")

if __name__ == "__main__":
    # Ejecutar Tolerancia a Fallos Bizantina
    print("Ejecutando Tolerancia a Fallos Bizantina:")
    byzantine_nodes = [ByzantineNode(i, is_faulty=(i % 2 == 0)) for i in range(5)]
    simulate_byzantine(byzantine_nodes)
    print()

    # Ejecutar Cristian
    print("Ejecutando Cristian:")
    server_time = datetime.now()
    cristian_nodes = [CristianNode(i, timedelta(seconds=random.randint(-300, 300))) for i in range(5)]
    cristian_algorithm(cristian_nodes, server_time)
    print()
