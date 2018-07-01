def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    if k > len(nums):
        k %= len(nums)
    l = len(nums[:-k])
    for i in range(l):
        nums.append(nums[i])
    del nums[:l]



nums = [1,2,3,4,5,6,7]
k = 3
print(rotate(nums, k))