def countPrimeSetBits(L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        c = 0
        for num in range(L, R + 1):
            set_bit = str(bin(num)[2:]).count('1')

            if set_bit == 2:
                c += 1
            elif set_bit > 2:
                for i in range(2, set_bit): 
                    if set_bit % i == 0:
                        c -= 1
                        break
                c += 1

        return c


L = 10
R = 15
print(countPrimeSetBits(L, R))