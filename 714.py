
def maxProfit(prices, fee):
    
    DP = [[0, 0] for i in range(len(prices))]
    DP[len(prices) - 1][1] = prices[len(prices) - 1] - fee
    
    for i in range(len(prices) - 2, -1, -1):
        for j in range(2):
            if j:
                DP[i][j] = max(prices[i] - fee + DP[i + 1][0], DP[i + 1][j])
            else:
                DP[i][j] = max(-prices[i] + DP[i + 1][1], DP[i + 1][j])
    
    print(DP)

    return DP[0][0]