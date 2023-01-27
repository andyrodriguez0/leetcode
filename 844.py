
def backspaceCompare(s, t):

    stack = []
    tack = []

    for i in range(len(s)):
        if stack and s[i] == '#':
            stack.pop()
        else:
            if s[i] == '#':
                continue
            else:
                stack.append(s[i])
    
    for i in range(len(t)):
        if tack and t[i] == '#':
            tack.pop()
        else:
            if t[i] == '#':
                continue
            else:
                tack.append(t[i])

    return stack == tack