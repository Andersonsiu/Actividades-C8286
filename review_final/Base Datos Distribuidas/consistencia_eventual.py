import threading
import time
import random 

class EventualConsistencyNode:
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

    def synchronize(self, other_node):
        with self.lock, other_node.lock:
            for key, value in other_node.data.items():
                if key not in self.data:
                    self.data[key] = value

def simulate_eventual_consistency(nodes):
    def writer(node, key, value):
        node.write(key, value)
        time.sleep(random.random())

    def reader(node, key):
        value = node.read(key)
        print(f"Node {node.node_id} read {key}: {value}")

    def synchronizer(node1, node2):
        node1.synchronize(node2)
        time.sleep(random.random())

    threads = []
    for i in range(5):
        writer_thread = threading.Thread(target=writer, args=(nodes[i % len(nodes)], f"key{i}", f"value{i}"))
        reader_thread = threading.Thread(target=reader, args=(nodes[i % len(nodes)], f"key{i}"))
        sync_thread = threading.Thread(target=synchronizer, args=(nodes[i % len(nodes)], nodes[(i + 1) % len(nodes)]))
        threads.append(writer_thread)
        threads.append(reader_thread)
        threads.append(sync_thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    nodes = [EventualConsistencyNode(i) for i in range(4)]
    simulate_eventual_consistency(nodes)
