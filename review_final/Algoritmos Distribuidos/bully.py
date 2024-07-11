
class Node:
    def __init__(self, node_id, nodes):
        self.node_id = node_id  # El número en la camiseta del amigo
        self.nodes = nodes  # La lista de todos los amigos
        self.leader = None  # El líder actual, al principio no hay líder

    def start_election(self):
        print(f"Nodo {self.node_id} inicia una elección.")
        higher_nodes = [node for node in self.nodes if node.node_id > self.node_id]
        if not higher_nodes:
            self.become_leader()
        else:
            for node in higher_nodes:
                if node.alive:
                    node.receive_election_message(self.node_id)

    def receive_election_message(self, sender_id):
        print(f"Nodo {self.node_id} recibe mensaje de elección desde el Nodo {sender_id}.")
        if self.node_id > sender_id:
            self.start_election()

    def become_leader(self):
        print(f"Nodo {self.node_id} llega a ser el líder.")
        self.leader = self.node_id
        for node in self.nodes:
            if node.node_id != self.node_id:
                node.leader = self.node_id

    @property
    def alive(self):
        return True

nodes = [Node(i, []) for i in range(5)]
for node in nodes:
    node.nodes = [n for n in nodes if n != node]

nodes[2].start_election()
