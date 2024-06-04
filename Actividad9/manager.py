from multiprocessing import Process, Manager

def increment(shared_dict, key):
    for _ in range(1000):
        shared_dict[key] += 1

if __name__ == "__main__":
    manager = Manager()
    shared_dict = manager.dict()
    shared_dict["counter"] = 0

    processes = []
    for _ in range(4):
        p = Process(target=increment, args=(shared_dict, "counter"))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f"Final counter value: {shared_dict['counter']}")
