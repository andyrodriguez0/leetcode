
from __future__ import annotations
import heapq

class Solution:
    def largestInteger(self, num: int) -> int:

        nums = list(str(num))
        odds = []
        evens = []

        for n in nums:
            if int(n) % 2:
                heapq.heappush(odds, -int(n))
            else:
                heapq.heappush(evens, -int(n))
        
        ans = []

        for n in nums:
            if int(n) % 2:
                ans.append(str(-heapq.heappop(odds)))
            else:
                ans.append(str(-heapq.heappop(evens)))
        
        return int(''.join(ans))

solution = Solution()
print(solution.largestInteger(1234))