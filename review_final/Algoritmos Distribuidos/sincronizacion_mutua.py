import threading
import random
from datetime import datetime, timedelta

# Algoritmo de Berkeley

class BerkeleyNode:
    def __init__(self, node_id, offset):
        self.node_id = node_id
        self.clock = datetime.now() + offset

    def adjust_clock(self, time_difference):
        self.clock += time_difference

def berkeley_algorithm(nodes):
    master_node = random.choice(nodes)
    master_time = master_node.clock
    time_differences = []

    for node in nodes:
        if node != master_node:
            time_difference = node.clock - master_time
            time_differences.append(time_difference)
            print(f"Node {node.node_id} clock difference: {time_difference}")

    average_time_difference = sum(time_differences, timedelta()) / len(nodes)
    print(f"Average time difference: {average_time_difference}")

    for node in nodes:
        node.adjust_clock(average_time_difference)
        print(f"Node {node.node_id} adjusted clock: {node.clock}")

# Algoritmo de Exclusión Mutua de Lamport

class LamportMutexNode:
    def __init__(self, node_id, num_nodes):
        self.node_id = node_id
        self.num_nodes = num_nodes
        self.clock = 0
        self.request_queue = queue.PriorityQueue()
        self.replies_received = 0

    def send_request(self):
        self.clock += 1
        self.request_queue.put((self.clock, self.node_id))
        for node in nodes:
            if node.node_id != self.node_id:
                node.receive_request(self.clock, self.node_id)

    def receive_request(self, timestamp, sender_id):
        self.clock = max(self.clock, timestamp) + 1
        self.request_queue.put((timestamp, sender_id))
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
        time.sleep(1)
        self.leave_critical_section()

    def leave_critical_section(self):
        print(f"Node {self.node_id} leaving critical section")
        self.replies_received = 0
        self.request_queue.get()

# Algoritmo de Marzullo (Para sincronización de tiempo precisa)
# Implementación simplificada

def marzullo_algorithm(time_intervals):
    best_start, best_end = -float('inf'), float('inf')
    for (start, end) in time_intervals:
        best_start = max(best_start, start)
        best_end = min(best_end, end)
    if best_start <= best_end:
        return best_start, best_end
    return None

if __name__ == "__main__":
    # Ejecutar Berkeley
    print("Ejecutando Berkeley:")
    berkeley_nodes = [BerkeleyNode(i, timedelta(seconds=random.randint(-300, 300))) for i in range(5)]
    berkeley_algorithm(berkeley_nodes)
    print()

    # Ejecutar Lamport Mutex
    print("Ejecutando Lamport Mutex:")
    lamport_nodes = [LamportMutexNode(i, 3) for i in range(3)]
    lamport_nodes[0].send_request()
    print()

    # Ejecutar Marzullo
    print("Ejecutando Marzullo:")
    intervals = [(1, 3), (2, 5), (0, 2)]
    result = marzullo_algorithm(intervals)
    print(f"Marzullo result: {result}")
