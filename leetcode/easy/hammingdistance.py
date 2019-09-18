def hammingDistance(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    x = bin(x)[2:].zfill(32)
    y = bin(y)[2:].zfill(32)
    c = 0
    for i in range(len(max(x, y))):
        if str(x)[i] != str(y)[i]:
            c += 1
    return c



x = 680142203
y = 1111953568
print(hammingDistance(x, y))