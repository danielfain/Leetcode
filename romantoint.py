class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        v = 0
        t = list(s)
        for i in range(1, len(s)):
            if values[s[i]] > values[s[i - 1]]:
                v += (values[s[i]] - values[s[i - 1]])
                t.remove(s[i])
                t.remove(s[i - 1])
        for numeral in t:
            v += values[numeral]
        return v

numeral = 'XXX' # The roman numeral to be solved

print(Solution.romanToInt(Solution(), numeral))