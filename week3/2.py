import threading


class MyThread:  # you need to inherit threading.Thread
    def __init__(self):  # you may add some other arguments
        pass

    def run(self):
        # run some task, or simply invoke time.sleep
        pass


if __name__ == "__main__":
    # write something to record the time consumption
    thds = [MyThread() for _ in range(10)]
    for thd in thds:
        thd.start()
    for thd in thds:
        thd.join()

    # write a single-threaded task that runs your task 10 times
    # record the time and compare it with the previous one
    pass
