def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    hm = {}
    while n != 1:
        if n in hm:
            return False
        else:
            hm[n] = True
        n = sum([int(i) ** 2 for i in str(n)])
    return True

    

n = 19
print(isHappy(n))