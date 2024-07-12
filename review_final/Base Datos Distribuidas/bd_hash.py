import hashlib

class HashPartitionedDatabase:
    def __init__(self, num_partitions):
        self.partitions = [{} for _ in range(num_partitions)]

    def _get_partition(self, key):
        hash_value = int(hashlib.sha256(key.encode()).hexdigest(), 16)
        return hash_value % len(self.partitions)

    def write(self, key, value):
        partition = self._get_partition(key)
        self.partitions[partition][key] = value

    def read(self, key):
        partition = self._get_partition(key)
        return self.partitions[partition].get(key, None)

def main():
    db = HashPartitionedDatabase(4)
    db.write("key1", "value1")
    db.write("key2", "value2")
    db.write("key3", "value3")

    print("Read key1:", db.read("key1"))
    print("Read key2:", db.read("key2"))
    print("Read key3:", db.read("key3"))

if __name__ == "__main__":
    main()
