import threading
from queue import Queue  # multithreading의 Queue
from multiprocessing import Queue  # multiprocessing의 Queue


def my_function(l):
    for i in range(10):
        l.append(i)


if __name__ == "__main__":
    my_list = []
    thread = threading.Thread(target=my_function, args=(my_list,))
    thread.start()
    thread.join()

    print(my_list)  # 메모리를 공유하기 때문에 출력된다.
    """
    메모리를 공유하기 때문에 생성 속도가 훨씬 빠르다. (메모리 생성 X)
    Process 하나 만드는데 0.1s.
    C/C++같은 low level에서는 thread 기반으로 코딩한다.
    """
