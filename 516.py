
def longestPalindromeSubseq(s):

        DP = [[0 for i in range(len(s))] for j in range(len(s))]

        for i in range(len(s)):
            DP[i][i] = 1
        
        for i in range(1, len(s)):
            for j in range(len(s) - i):

                row = j
                col = j + i

                first = float('-inf')
                second = float('-inf')
                third = float('-inf')
                
                for k in range(col, row, -1):
                    if s[row] == s[k]:
                        first = 2 + DP[row + 1][k - 1]
                        break
                
                for k in range(row, col):
                    if s[col] == s[k]:
                        second = 2 + DP[k + 1][col - 1]
                        break

                third = DP[row + 1][col - 1]

                DP[row][col] = max(first, second, third, 1)
        
        return(DP[0][len(s) - 1])