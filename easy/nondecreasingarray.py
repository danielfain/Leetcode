def checkPossibility(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        f, l = nums[:], nums[:]
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                f[i] = nums[i + 1]
                l[i + 1] = nums[i]
                break
        
        return f == sorted(f) or l == sorted(l)


        


nums = [4,2,3]
print(checkPossibility(nums))