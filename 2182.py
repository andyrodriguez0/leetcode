
from collections import Counter
import heapq

def repeatLimitedString(s, repeatLimit):

    counts = Counter(s)
    heap = []
    k = repeatLimit

    for char in counts:
        heapq.heappush(heap, (-ord(char), char, counts[char]))
    
    ans = []

    while heap:
        print(heap)
        to_add = heapq.heappop(heap)
        if to_add[2] <= k:
            ans.append(to_add[1] * to_add[2])
        else:
            ans.append(to_add[1] * k)
            if heap:
                to_add_next = heapq.heappop(heap)
                ans.append(to_add_next[1])
                heapq.heappush(heap, (-ord(to_add[1]), to_add[1], to_add[2] - k))
                if to_add[2] - 1:
                    heapq.heappush(heap, (-ord(to_add_next[1]), to_add_next[1], to_add[2] - 1))
    
    return ''.join(ans)