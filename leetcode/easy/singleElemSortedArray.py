def singleNonDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l = 0
    r = len(nums) - 1
    
    while r >= l:
        if nums[l] == nums[l+1]:
            l += 2
        else:
            return nums[l]
        if nums[r] == nums[r-1]:
            r -= 2
        else:
            return nums[r]


nums = [1,1,2,3,3,4,4,8,8]
print(singleNonDuplicate(nums))