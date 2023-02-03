
from __future__ import annotations

class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stack = []

        for operation in operations:
            if operation == '+':
                score1 = stack.pop()
                score2 = stack.pop()
                score3 = score1 + score2
                stack.append(score2)
                stack.append(score1)
                stack.append(score3)
            elif operation == 'D':
                score1 = stack.pop()
                score2 = score1 * 2
                stack.append(score1)
                stack.append(score2)
            elif operation == 'C':
                stack.pop()
            else:
                stack.append(int(operation))

        return sum(stack)

solution = Solution()
print(solution.calPoints(["5","-2","4","C","D","9","+","+"]))