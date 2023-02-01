
def minPathSum(grid):

    m = len(grid)
    n = len(grid[0])

    DP = [[0 for j in range(n)] for i in range(m)]

    DP[0][0] = grid[0][0]

    for i in range(1, m):
        DP[i][0] = grid[i][0] + DP[i - 1][0]

    for j in range(1, n):
        DP[0][j] = grid[0][j] + DP[0][j - 1]

    for i in range(1, m):
        for j in range(1, n):
            DP[i][j] = grid[i][j] + min(DP[i - 1][j], DP[i][j - 1])

    return DP[m - 1][n - 1]