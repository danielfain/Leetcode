def simplifyPath(path: 'str') -> 'str':
    stack = []
    string = path.split('/')
    res = ''

    for s in string:
        if s:
            if s == '..':
                if len(stack) >= 1:
                    stack.pop()
            elif s == '.':
                pass
            else:
                stack.append(s)
    
    for part in stack:
        res += '/' + part
    if res:
        return res
    return '/'