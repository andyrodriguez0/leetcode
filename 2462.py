
import heapq

def totalCost(costs, k, candidates):

    heap = []

    for i in range(candidates):
        heapq.heappush(heap, (costs[i], i))
        heapq.heappush(heap, (costs[-i - 1], len(costs) - i))

    left = candidates
    right = len(costs) - candidates - 1
    cost = 0

    while k > 0:
        to_add = heapq.heappop(heap)
        cost += to_add[0]
        k -= 1
        if left <= right:
            if to_add[1] <= left:
                heapq.heappush(heap, (costs[left], left))
                left += 1
            else:
                heapq.heappush(heap, (costs[right], right))
                right -= 1
    
    return cost