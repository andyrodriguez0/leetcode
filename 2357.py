
from __future__ import annotations
import heapq

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        target = max(nums)
        heapq.heapify(nums)
        add = 0
        count = 0

        while target > 0:
            sub = heapq.heappop(nums) - add
            if sub:
                target -= sub
                add += sub
                count += 1
                print(target)
        

        return count

solution = Solution()
print(solution.minimumOperations([1,5,0,3,5]))