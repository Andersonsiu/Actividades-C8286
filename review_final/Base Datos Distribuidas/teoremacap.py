import random
import threading
import time

class Node:
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

class NetworkPartition:
    def __init__(self, nodes):
        self.nodes = nodes

    def create_partition(self):
        partitioned_nodes = random.sample(self.nodes, len(self.nodes) // 2)
        for node in partitioned_nodes:
            node.lock.acquire()

    def resolve_partition(self):
        for node in self.nodes:
            if node.lock.locked():
                node.lock.release()

def simulate_cap(nodes, mode):
    partition = NetworkPartition(nodes)
    if mode in ["CP", "AP"]:
        partition.create_partition()
    
    def writer(node, key, value):
        node.write(key, value)
        time.sleep(random.random())

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

    if mode in ["CP", "AP"]:
        partition.resolve_partition()

if __name__ == "__main__":
    nodes = [Node(i) for i in range(4)]
    print("Simulating CP mode")
    simulate_cap(nodes, "CP")
    print("\nSimulating AP mode")
    simulate_cap(nodes, "AP")
    print("\nSimulating CA mode")
    simulate_cap(nodes, "CA")
