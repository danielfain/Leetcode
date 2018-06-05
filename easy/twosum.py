def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for x in range(1, len(nums)):
                if nums[x] == target - nums[i] and i != x:
                    return [i, x]



nums = [3,2,4]
target = 6
print(twoSum(nums, target))