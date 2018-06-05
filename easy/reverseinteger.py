def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        elif x > 0:
            r = list(reversed(str(x)))
            n = r[:]
            for i in r:
                if i == '0':
                    n.remove(i)
                else:
                    break

            number = int(''.join(n))
            if not(int(number)>>31):
                return number
            else:
                return 0
        else:
            r = list(reversed(str(abs(x))))
            n = r[:]
            for i in r:
                if i == '0':
                    n.remove(i)
                else:
                    break

            number = int('-' + ''.join(n))
            if not(int(abs(number))>>31):
                return number
            else:
                return 0
        

x = 1563847412
print(reverse(x))