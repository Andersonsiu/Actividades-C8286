import threading
import random

# Algoritmo de Paxos

class PaxosNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.proposal_number = 0
        self.accepted_proposal_number = -1
        self.accepted_value = None
        self.promised_proposal_number = -1

    def prepare(self, proposal_number):
        if proposal_number > self.promised_proposal_number:
            self.promised_proposal_number = proposal_number
            return self.accepted_proposal_number, self.accepted_value
        return None

    def accept(self, proposal_number, value):
        if proposal_number >= self.promised_proposal_number:
            self.promised_proposal_number = proposal_number
            self.accepted_proposal_number = proposal_number
            self.accepted_value = value
            return True
        return False

    def consensus(self, nodes, value):
        self.proposal_number += 1
        promises = []
        for node in nodes:
            promise = node.prepare(self.proposal_number)
            if promise:
                promises.append(promise)
        
        if len(promises) > len(nodes) // 2:
            for node in nodes:
                node.accept(self.proposal_number, value)
            self.accepted_value = value
        return self.accepted_value

def simulate_paxos(nodes, value):
    leader = random.choice(nodes)
    consensus_value = leader.consensus(nodes, value)
    return consensus_value

# Algoritmo de Bully

class Node:
    def __init__(self, node_id, nodes):
        self.node_id = node_id
        self.nodes = nodes
        self.coordinator = None

    def start_election(self):
        print(f"Node {self.node_id} starts an election.")
        higher_nodes = [node for node in self.nodes if node.node_id > self.node_id]
        if not higher_nodes:
            self.become_coordinator()
        else:
            for node in higher_nodes:
                node.receive_election_message(self.node_id)

    def receive_election_message(self, sender_id):
        print(f"Node {self.node_id} received election message from Node {sender_id}.")
        self.start_election()

    def become_coordinator(self):
        self.coordinator = self.node_id
        for node in self.nodes:
            node.coordinator = self.node_id
        print(f"Node {self.node_id} is the new coordinator.")

if __name__ == "__main__":
    # Ejecutar Paxos
    print("Ejecutando Paxos:")
    paxos_nodes = [PaxosNode(i) for i in range(5)]
    paxos_value = "Update Inventory Record"
    agreed_value = simulate_paxos(paxos_nodes, paxos_value)
    print(f"Agreed Value: {agreed_value}\n")

    # Ejecutar Bully
    print("Ejecutando Bully:")
    bully_nodes = [Node(i, []) for i in range(5)]
    for node in bully_nodes:
        node.nodes = [n for n in bully_nodes if n != node]
    bully_nodes[2].start_election()
    print()
