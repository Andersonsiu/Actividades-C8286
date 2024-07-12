import threading
import time

class SynchronousReplicationNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.data = {}
        self.lock = threading.Lock()

    def write(self, key, value):
        with self.lock:
            self.data[key] = value

    def read(self, key):
        with self.lock:
            return self.data.get(key, None)

    def replicate(self, key, value):
        self.write(key, value)

def simulate_synchronous_replication(nodes):
    def writer(node, key, value):
        node.write(key, value)
        for n in nodes:
            if n != node:
                n.replicate(key, value)

    def reader(node, key):
        value = node.read(key)
        print(f"Node {node.node_id} read {key}: {value}")

    threads = []
    for i in range(5):
        writer_thread = threading.Thread(target=writer, args=(nodes[i % len(nodes)], f"key{i}", f"value{i}"))
        reader_thread = threading.Thread(target=reader, args=(nodes[i % len(nodes)], f"key{i}"))
        threads.append(writer_thread)
        threads.append(reader_thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    nodes = [SynchronousReplicationNode(i) for i in range(4)]
    simulate_synchronous_replication(nodes)
