
from __future__ import annotations
import heapq

class Solution:
    def fillCups(self, amount: List[int]) -> int:

        amount = [-i for i in amount if i]
        heapq.heapify(amount)
        count = 0

        while amount:

            if len(amount) > 1:
                one = -heapq.heappop(amount)
                two = -heapq.heappop(amount)
                if one and one - 1:
                    heapq.heappush(amount, -(one - 1))
                if two and two - 1:
                    heapq.heappush(amount, -(two - 1))
                count += 1
            
            else:
                one = -heapq.heappop(amount)
                if one and one - 1:
                    heapq.heappush(amount, -(one - 1))
                count += 1
        
        return count

solution = Solution()
print(solution.fillCups([1, 4, 2]))