
def longestCommonSubsequence(text1, text2):

    DP = [[0 for i in range(len(text2))] for i in range(len(text1))]

    for i in range(len(text1)):
        for j in range(len(text2)):
            if text1[i] == text2[j]:
                if i and j:
                    DP[i][j] = 1 + DP[i - 1][j - 1]
                else:
                    DP[i][j] = 1
            else:
                DP[i][j] = max(DP[i - 1][j], DP[i][j - 1])

    return DP[len(text1) - 1][len(text2) - 1]