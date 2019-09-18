def shortestToChar(S, C):
    """
    :type S: str
    :type C: str
    :rtype: List[int]
    """
    l = []
    last = None
    for i, x in enumerate(S):
        if x == C:
            last = i
        if last == None:
            l.append(S.find(C) - i)
        else:
            lastdif = abs(last - i)
            cdif = abs(S.find(C, i) - i)
            if lastdif <= cdif:
                l.append(lastdif)
            else:
                l.append(cdif)
    return l


S = 'aaba'
C = 'b'
print(shortestToChar(S, C))
