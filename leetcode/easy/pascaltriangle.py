def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    pt = [[1] for i in range(numRows)]
    for i in range(1, numRows):
    	if len(pt[i-1]) == 1:
    		pt[i].append(1)
    	else:
    		for x in range(len(pt[i-1])):
    			try:
    				n = pt[i-1][x] + pt[i-1][x+1]
    				pt[i].append(n)
    			except IndexError:
    				pt[i].append(1)
    				break

    return pt




numRows = 5
print(generate(numRows))


