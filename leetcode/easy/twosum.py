def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hm = {}
        
    for i in range(len(nums)):
        if target - nums[i] in hm:
            return sorted([i, hm[target - nums[i]]])
        else:
            hm[nums[i]] = i


nums = [2, 2, 11, 15, 18]
target = 20
print(twoSum(nums, target))