def lengthOfLastWord(s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s == " " * len(s):
            return 0
        else:
            if not s[-1] == ' ':
                return len(s.split(' ')[-1])
            else:
                c = 0
                while True:
                    c -= 1
                    if s.split(' ')[c] != '':
                        return len(s.split(' ')[c])


s = "  a    b  "
print(lengthOfLastWord(s))