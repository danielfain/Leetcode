def addUpToK(nums, k):
    hm = {}
    for num in nums:
        dif = num - k
        if dif in hm:
            if dif + num == k:
                return True
            else:
                hm[num] = 1
        else:
            hm[num] = 1

    return False

nums = [10, 15, 3, 7, 2]
k = 6
print(addUpToK(nums, k))

