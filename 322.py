
def coinChange(coins, amount):
    
    if not amount:
        return 0
    elif min(coins) > amount:
        return -1
    
    DP = [-1] * amount
    DP[min(coins) - 1] = 1
    
    for i in range(min(coins), amount):
        for coin in coins:
            if i - coin >= 0 and DP[i - coin] != -1:
                if DP[i] != -1:
                    DP[i] = min(1 + DP[i - coin], DP[i])
                else:
                    DP[i] = 1 + DP[i - coin]
            if coin == i + 1:
                if DP[i] != -1:
                    DP[i] = min(1, DP[i])
                else:
                    DP[i] = 1

    return DP[amount - 1]