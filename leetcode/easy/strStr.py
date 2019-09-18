def strStr(haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack:
            return haystack.find(needle)
        elif needle == '':
            return 0
        else:
            return -1

haystack = "aaaaa"
needle = "bba"
print(strStr(haystack, needle))