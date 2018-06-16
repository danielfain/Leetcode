def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1:
    	return 1
    else:
	    arr = [0] * n
	    arr[0], arr[1] = 1, 2

	    for i in range(2, n):
	    	arr[i] = arr[i-1] + arr[i-2]

	    return arr[-1]





n = 5
print(climbStairs(n))
    