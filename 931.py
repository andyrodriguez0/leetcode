
def minFallingPathSum(matrix):
    
    n = len(matrix)
    
    DP = [[float('inf') for i in range(n)] for j in range(n)]
    
    for j in range(n):
        DP[0][j] = matrix[0][j]
    
    for i in range(1, n):
        for j in range(n):
            if not j:
                DP[i][j] = matrix[i][j] + min(DP[i - 1][j], DP[i - 1][j + 1])
            elif j == n - 1:
                DP[i][j] = matrix[i][j] + min(DP[i - 1][j - 1], DP[i - 1][j])
            else:
                DP[i][j] = matrix[i][j] + min(DP[i - 1][j - 1], DP[i - 1][j], DP[i - 1][j + 1])

    return min(DP[n - 1])