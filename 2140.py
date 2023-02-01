
def mostPoints(questions):

    DP = [0] * len(questions)
    DP[0] = questions[0][0]

    for i in range(1, len(questions)):
        for j in range(i):
            if i - j > questions[j][1]:
                DP[i] = max(questions[i][0] + DP[j], DP[i])
        DP[i] = max(questions[i][0], DP[i])

    return DP[len(questions) - 1]