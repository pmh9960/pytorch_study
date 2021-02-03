import multiprocessing as mp
import numpy as np


def f_lock(lock, num):
    lock.acquire()
    print("hello world", num)
    lock.release()
    # Or use
    with lock:
        print("hello world", num)


def f_queue(queue):
    for num in range(3):
        queue.put(num)
    queue.put(None)


if __name__ == "__main__":
    lock = mp.Lock()
    queue = mp.Queue(maxsize=2)

    # Lock
    for num in range(3):
        mp.Process(target=f_lock, args=(lock, num)).start()

    mp.Process(target=f_queue, args=(queue,)).start()
    while True:
        var = queue.get()
        print(var)
        if var is None:
            break  # 없으면 Deadlock 걸림 무한히 get을 기다림
    print("Good")
