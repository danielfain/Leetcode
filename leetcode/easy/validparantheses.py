def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    hm = {'}': '{', ']': '[', ')': '('}

    for char in s:
        if char in hm:
            try:
                if stack.pop() != hm[char]:
                    return False
            except:
                return False
        else:
            stack.append(char)
    return not stack


s = "[[[]]]"
print(isValid(s))