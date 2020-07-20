def removeElement(nums, val):
    length = len(nums)
    for i in range(len(nums)):
        if (nums[i] == val):
            nums[i] = nums[length - 1]
            length -= 1    

    return length

nums = [3,2,2,3]
val = 3
removeElement(nums, val)
print(nums)