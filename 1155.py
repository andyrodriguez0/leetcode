
from __future__ import annotations

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        DP = {}
        for i in range(1, k + 1):
            DP[(i, 1)] = 1

        for i in range(1, target + 1):
            for j in range(2, n + 1):
                print()
                add = 0
                for m in range(1, k + 1):
                    add += DP.get((i - m, j - 1), 0)
                DP[(i, j)] = add

        return DP.get((target, n), 0) % (10 ** 9 + 7)

solution = Solution()
print(solution.numRollsToTarget(1, 2, 3))