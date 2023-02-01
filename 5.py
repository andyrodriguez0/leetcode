class Solution:
    def longestPalindrome(self, s: str) -> str:

        DP = [[0 for i in range(len(s))] for i in range(len(s))]

        for i in range(len(s)):
            DP[i][i] = 1
        
        longest = 1
        indices = (0, 0)

        for length in range(1, len(s)):
            for start in range(len(s) - length):

                i = start
                j = start + length

                if s[i] == s[j]:
                    if i == j - 1 or DP[i + 1][j - 1]:
                        DP[i][j] = 2 + DP[i + 1][j - 1]
                    if DP[i][j] > longest:
                        longest = DP[i][j]
                        indices = (i, j)
        
        string = s[indices[0]:indices[1] + 1]

        return string