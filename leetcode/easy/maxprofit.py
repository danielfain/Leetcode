def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    minprice = 1000000000000000000
    maxprofit = 0
    for i in range(len(prices)):
        if prices[i] < minprice:
            minprice = prices[i]
        elif prices[i] - minprice > maxprofit:
            maxprofit = prices[i] - minprice
    return maxprofit




prices = [2,4,10]
print(maxProfit(prices))
    