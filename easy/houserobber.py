def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0

    for i in range(len(nums)):
        if i == 1:
            nums[i] = max(nums[0], nums[1])
        if i > 1:
            nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])

    return max(nums)








nums = [9,2,9,3,1]
print(rob(nums))
    