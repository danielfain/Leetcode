def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        w = ''
        i = 0
        if strs == []:
            return w
        else:
            for _ in range(len(min(strs))):
                for word in strs:
                    if word[i] != strs[0][i]:
                        break
                else:
                    w += word[i]
                    i += 1
        return w



strs = ['flower', 'flow', 'flock']
print(longestCommonPrefix(strs))