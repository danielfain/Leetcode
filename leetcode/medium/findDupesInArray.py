def findDuplicates(nums):
    hm = {}
    dupes = []
    
    for i in range(len(nums)):
        if nums[i] in hm:
            dupes.append(nums[i])
        else:
            hm[nums[i]] = True
        
    return dupes

nums = [4,3,2,7,8,2,3,1]
print(findDuplicates(nums))