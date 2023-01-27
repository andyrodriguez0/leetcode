
def isValid(s):

    stack = []

    stack.append(s[0])

    for i in range(1, len(s)):
        if s[i] == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s[i])
        elif s[i] == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                stack.append(s[i])
        elif s[i] == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])

    return not stack