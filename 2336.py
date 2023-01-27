
import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.counter = 0
        self.can_add = set()

    def popSmallest(self):
        if self.heap and self.heap[0] < self.counter + 1:
            return heapq.heappop(self.heap)
        else:
            self.counter += 1
            self.can_add.add(self.counter)
            return self.counter

    def addBack(self, num):
        if num in self.can_add:
            heapq.heappush(self.heap, num)
            self.can_add.remove(num)