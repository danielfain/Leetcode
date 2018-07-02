def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    hm = {}
    for num in set(nums):
        hm[num] = nums.count(num)
    for key in hm:
        if hm[key] > len(nums) / 2:
            return key


nums = [3, 2, 3]
print(majorityElement(nums))
