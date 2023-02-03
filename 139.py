
from __future__ import annotations

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        DP = [0 for _ in range(len(s))]

        for i in range(len(s)):

            if s[:i + 1] in wordDict:
                DP[i] = 1
                continue

            for j in range(i):
                if DP[j] and s[j + 1:i + 1] in wordDict:
                    DP[i] = 1
                    break

        return bool(DP[-1])

solution = Solution()
print(solution.wordBreak('ab', ["a","b"]))