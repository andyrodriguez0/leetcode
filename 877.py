
from __future__ import annotations

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        DP = [[0 for _ in range(len(piles))] for _ in range(len(piles))]

        for i in range(len(piles)):
            DP[i][i] = piles[i]
        
        for i in range(len(piles) - 1):
            DP[i][i + 1] = max(piles[i], piles[i + 1])
        
        for i in range(len(piles) - 2):
            if piles[i] > piles[i + 2]:
                DP[i][i + 2] = piles[i] + min(piles[i + 1], piles[i + 2])
            else:
                DP[i][i + 2] = piles[i + 2] + min(piles[i], piles[i + 1])
        
        for length in range(3, len(piles)):
            for start in range(len(piles) - length):
                
                i = start
                j = start + length

                DP[i][j] = max(piles[i] + min(DP[i + 2][j], DP[i + 1][j - 1]), piles[j] + min(DP[i + 1][j - 1], DP[i][j - 2]))
        
        print(DP)

        return DP[0][len(piles) - 1] > sum(piles) / 2

solution = Solution()
print(solution.stoneGame([5,3,4,5]))