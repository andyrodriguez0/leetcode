
def generate(numRows):

    ans = []

    for row in range(numRows):
        insert = []
        for col in range(row + 1):
            if not col:
                insert.append(1)
            elif col == row:
                insert.append(1)
            else:
                insert.append(ans[row - 1][col - 1] + ans[row - 1][col])
        ans.append(insert)
    
    return ans