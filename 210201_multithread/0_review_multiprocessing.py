import multiprocessing as mp


def my_function(l):
    for i in range(10):
        l.append(i)


if __name__ == "__main__":
    my_list = []
    process = mp.Process(target=my_function, args=(my_list,))
    process.start()
    process.join()

    # Using multiprocessing
    print(my_list)

    # Using reference
    my_function(my_list)
    print(my_list)

    # Or using queue or lock
