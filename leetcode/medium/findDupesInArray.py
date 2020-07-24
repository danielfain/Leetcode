def findDuplicates(nums):
    dupes = []
        
    for num in nums:
        i = abs(num) - 1
        
        if nums[i] < 0:
            dupes.append(abs(num))
        else:
            nums[i] = nums[i] * -1
        
    return dupes

nums = [4,3,2,7,8,2,3,1]
print(findDuplicates(nums))