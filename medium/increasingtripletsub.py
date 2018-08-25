def increasingTriplet(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    for i in range(2, len(nums)):
        try:
            if nums[i] > nums[i-1] and nums[i-1] > nums[i-2]:
                return True
        except:
            return False
    return False




nums = [5,1,5,1,4,6,4]
print(increasingTriplet(nums))

