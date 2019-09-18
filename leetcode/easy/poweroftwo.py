def isPowerOfTwo(n):
    """
    :type n: int
    :rtype: bool
    """
    if n == 1:
        return True
    elif n % 2 == 0:
        for i in range(1, n):
            if 2 ** i == n:
                return True
            elif 2 ** i > n:
                return False
    return False



n = 5010
print(isPowerOfTwo(n))
