def repeatedStringMatch(A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        l = A
        c = 1

        for i in range(len(B)):
            if B in l:
                return c
            else:
                l += A
                c += 1

        return -1


A = 'abababaaba'
B = 'aabaaba'
print(repeatedStringMatch(A, B))