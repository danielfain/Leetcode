def searchInsert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            n = nums[:]
            n.append(target)
            return sorted(n).index(target)

nums = [1,3,5,6]
target = 0
print(searchInsert(nums, target))