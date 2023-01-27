
def simplifyPath(path):
    
    path = path.split('/')
    
    stack = ['/']

    for char in path:
        if char == '..':
            if len(stack) >= 3:
                stack.pop()
                stack.pop()
        elif char and char != '.':
            stack.append(char)
        if stack[-1] != '/':
            stack.append('/')



    if stack[-1] == '/' and len(stack) > 2:
        stack.pop()
    
    return ''.join(stack)