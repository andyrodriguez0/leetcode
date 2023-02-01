
def maxProfit(prices):
    
    DP = {}
        
    DP[(len(prices) - 1, 1, 0)] = prices[len(prices) - 1]
    DP[(len(prices) - 1, 0, 1)] = 0
    DP[(len(prices) - 1, 0, 0)] = 0
    
    for i in range(len(prices) - 2, -1, -1):
        for j in range(2):
            for k in range(2):
                if j and k:
                    continue
                elif j:
                    DP[(i, j, k)] = max(prices[i] + DP[(i + 1, 0, 1)], DP[(i + 1, j, k)])
                else:
                    if k:
                        DP[(i, j, k)] = DP[(i + 1, j, 0)]
                    else:
                        DP[(i, j, k)] = max(-prices[i] + DP[(i + 1, 1, k)], DP[(i + 1, j, k)])
    
    print(DP)

    return DP[(0, 0, 0)]

print(maxProfit([1,2,3,0,2]))