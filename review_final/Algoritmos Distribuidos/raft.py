import threading
import time

class Node:
    def __init__(self, node_id, peers):
        self.node_id = node_id
        self.peers = peers
        self.term = 0
        self.voted_for = None
        self.state = "follower"
        self.log = []
        self.commit_index = 0
        self.last_applied = 0

    def start_election(self):
        self.state = "candidate"
        self.term += 1
        self.voted_for = self.node_id
        votes = 1
        for peer in self.peers:
            if peer.request_vote(self.term, self.node_id):
                votes += 1
        if votes > len(self.peers) / 2:
            self.state = "leader"
            self.lead()

    def request_vote(self, term, candidate_id):
        if term > self.term:
            self.term = term
            self.voted_for = candidate_id
            return True
        return False

    def lead(self):
        while self.state == "leader":
            self.send_heartbeats()
            time.sleep(1)

    def send_heartbeats(self):
        for peer in self.peers:
            peer.receive_heartbeat(self.term, self.node_id)

    def receive_heartbeat(self, term, leader_id):
        if term >= self.term:
            self.term = term
            self.state = "follower"

# Ejemplo de uso
nodes = [Node(i, []) for i in range(5)]
for node in nodes:
    node.peers = [n for n in nodes if n != node]

leader = nodes[0]
thread = threading.Thread(target=leader.start_election)
thread.start()
