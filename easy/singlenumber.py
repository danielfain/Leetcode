def singleNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
            print(hash_table)
        return hash_table.popitem()[0]
        

nums = [1,1,2,2,3,4,4]
print(singleNumber(nums))