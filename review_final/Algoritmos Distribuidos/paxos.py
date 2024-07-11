class Proposer:
    def __init__(self, proposer_id, acceptors):
        self.proposer_id = proposer_id
        self.acceptors = acceptors
        self.proposal_number = 0
        self.proposal_value = None

    def prepare(self):
        self.proposal_number += 1
        promises = []
        for acceptor in self.acceptors:
            promise = acceptor.receive_prepare(self.proposal_number)
            if promise:
                promises.append(promise)
        if len(promises) > len(self.acceptors) / 2:
            self.propose()

    def propose(self):
        for acceptor in self.acceptors:
            acceptor.receive_propose(self.proposal_number, self.proposal_value)

class Acceptor:
    def __init__(self, acceptor_id):
        self.acceptor_id = acceptor_id
        self.promised_proposal_number = 0
        self.accepted_proposal_number = 0
        self.accepted_value = None

    def receive_prepare(self, proposal_number):
        if proposal_number > self.promised_proposal_number:
            self.promised_proposal_number = proposal_number
            return (self.accepted_proposal_number, self.accepted_value)
        return None

    def receive_propose(self, proposal_number, value):
        if proposal_number >= self.promised_proposal_number:
            self.promised_proposal_number = proposal_number
            self.accepted_proposal_number = proposal_number
            self.accepted_value = value
            return True
        return False

# Ejemplo de uso
acceptors = [Acceptor(i) for i in range(5)]
proposer = Proposer(1, acceptors)
proposer.prepare()
