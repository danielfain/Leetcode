def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        if len(str(x)) == 1:
            return True
        else:
            l = list(str(x))

            if l == list(reversed(l)):
                return True
            else:
                return False


x = 'racecar'
print(isPalindrome(x))