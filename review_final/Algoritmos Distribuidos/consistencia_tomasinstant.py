import threading
import random
import queue
import time
from datetime import datetime, timedelta

# Algoritmo de Raft

class RaftNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.term = 0
        self.voted_for = None
        self.log = []

    def request_vote(self, term, candidate_id):
        if term > self.term:
            self.term = term
            self.voted_for = candidate_id
            return True
        return False

    def append_entries(self, term, leader_id, entries):
        if term >= self.term:
            self.term = term
            self.log.extend(entries)
            return True
        return False

def simulate_raft(nodes, entries):
    leader = random.choice(nodes)
    for node in nodes:
        if node != leader:
            node.append_entries(leader.term, leader.node_id, entries)
    return leader.log

# Algoritmo de Chandy-Lamport

class ChandyLamportNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.state = None
        self.channel = queue.Queue()

    def record_state(self):
        self.state = f"State of node {self.node_id}"

    def send_marker(self, nodes):
        for node in nodes:
            if node != self:
                node.channel.put(f"Marker from {self.node_id}")

    def receive_marker(self):
        while not self.channel.empty():
            marker = self.channel.get()
            print(f"Node {self.node_id} received {marker}")

def simulate_chandy_lamport(nodes):
    initiator = random.choice(nodes)
    initiator.record_state()
    initiator.send_marker(nodes)
    for node in nodes:
        node.receive_marker()

if __name__ == "__main__":
    # Ejecutar Raft
    print("Ejecutando Raft:")
    raft_nodes = [RaftNode(i) for i in range(5)]
    raft_entries = ["Transaction 1", "Transaction 2"]
    raft_log = simulate_raft(raft_nodes, raft_entries)
    print(f"Raft log: {raft_log}\n")

    # Ejecutar Chandy-Lamport
    print("Ejecutando Chandy-Lamport:")
    chandy_nodes = [ChandyLamportNode(i) for i in range(5)]
    simulate_chandy_lamport(chandy_nodes)
    print()
