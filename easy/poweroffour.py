def isPowerOfFour(num):
    """
    :type num: int
    :rtype: bool
    """
    ans = 0
    while 4 ** ans <= num:
        if 4 ** ans == num:
            return True
        ans += 1
    return False




num = 16
print(isPowerOfFour(num))