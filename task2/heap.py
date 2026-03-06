class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap)-1)

    def _heapify_up(self, i):
        p = (i-1)//2
        if i > 0 and self.heap[i] > self.heap[p]:
