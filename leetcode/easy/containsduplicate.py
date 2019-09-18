def containsDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hm = {}
        for num in nums:
            if num in hm:
                return True
            else:
                hm[num] = 0

        return False



nums = [1,1,1,3,3,4,3,2,4,2] 
print(containsDuplicate(nums))