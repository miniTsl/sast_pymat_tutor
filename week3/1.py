from queue import Empty, Full
# you may use heapq to check your implementation
import heapq


class PriorityQueue:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        # ...

    def __len__(self):
        # return current queue size
        pass

    def get(self):
        if len(self) == 0:
            raise Empty
        # put into queue
        pass

    def put(self, x):
        if len(self) >= self.maxsize:
            raise Full
        # get from queue
        pass
