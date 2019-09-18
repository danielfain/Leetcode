def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    c = 0
    for num in nums:
    	if num == 0:
    		c += 1

    for i in range(c):
    	nums.remove(0)
    	nums.append(0)



nums = [0,0,1]
print(moveZeroes(nums))
