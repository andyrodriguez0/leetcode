
import heapq

class KthLargest:

    def __init__(self, k, nums):
        
        self.k = k
        self.max_heap = []
        self.min_heap = []
        
        for num in nums:
            
            heapq.heappush(self.max_heap, -num)
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
            
        while len(self.min_heap) > self.k:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def add(self, val):
        
        heapq.heappush(self.max_heap, -val)
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        while len(self.min_heap) > self.k:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

        return self.min_heap[0]