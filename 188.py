
def maxProfit(k, prices):

    DP = {}

    for i in range(1, len(prices) + 1):
        for j in range(1, k + 1):
            DP[(i, i, j)] = 0
    
    for i in range(1, len(prices)):
        DP[(i, i + 1, 1)] = max(prices[i] - prices[i - 1], 0)
    
    for i in range(len(prices)):
        for j in range(len(prices)):
            DP[(i + 1, j + 1, 0)] = 0
    
    for m in range(1, k + 1):
        for length in range(2, len(prices)):
            for start in range(1, len(prices) - length + 1):

                i = start
                j = start + length
                curr = float('-inf')

                for l in range(i, j):
                    curr = max(DP[(i, l, m - 1)] + DP[(l + 1, j, 1)], DP[(i, l, 1)] + DP[(l + 1, j, m - 1)], curr)
                
                DP[(i, j, m)] = curr

    return DP[(1, len(prices), k)]