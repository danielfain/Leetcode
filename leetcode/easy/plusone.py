def plusOne(digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digs = [str(i) for i in digits]
        num = ''.join(digs)
        num = int(num) + 1
        return [int(i) for i in str(num)]



digits = [1,2,3]
print(plusOne(digits))