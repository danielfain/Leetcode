def selfDividingNumbers(left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        l = []
        for i in range(left, right + 1):
            if '0' not in str(i):
                d = None
                for num in str(i):
                    if int(i) % int(num) != 0:
                        d = False
                        break
                    else:
                        d = True
                if d == True:
                    l.append(int(i))


        return l


left = 1
right = 22
print(selfDividingNumbers(left, right))