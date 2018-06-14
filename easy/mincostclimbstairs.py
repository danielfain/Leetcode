def minCostClimbingStairs(cost):
    """
    :type cost: List[int]
    :rtype: int
    """
    l = [0] * len(cost)
    l[0], l[1] = cost[0], cost[1]
    for i in range(2, len(cost)):
        l[i] = min(l[i-2] + cost[i], l[i-1] + cost[i])

    return min(l[-1], l[-2])
        




cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(minCostClimbingStairs(cost))
    

