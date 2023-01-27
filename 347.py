
import heapq

def topKFrequent(nums, k):

    frequencies = {}

    for num in nums:
        frequencies[num] = frequencies.get(num, 0) + 1
    
    heap = []

    for frequency in frequencies:
        heapq.heappush(heap, (frequencies[frequency], frequency))
        if len(heap) > k:
            heapq.heappop(heap)

    ans = []

    for tup in heap:
        ans.append(tup[1])
    
    return ans