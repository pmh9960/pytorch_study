import numpy as np
import multiprocessing as mp


def function(var):
    var += 1
    print(var)

    return


if __name__ == "__main__":
    var = np.ones((10,))
    process = mp.Process(target=function, args=(var,))
    # process = mp.Process(target=function)  # Can use global variable either. (if OS use fork() not spawn())
    process.start()

    print("hello")
    # In debugging you can see two yellow line. (Python Current File & Subprocess ####)
    process.join()  # Parent process is waiting for subprocess
    print("good")

