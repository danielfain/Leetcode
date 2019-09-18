def wordPattern(pattern, str):
    """
    :type pattern: str
    :type str: str
    :rtype: bool
    """
    hm = {}
    if len(pattern) == len(str.split(' ')) and len(set(pattern)) == len(set(str.split(' '))):
        for i in range(len(pattern)):
            if str.split(' ')[i] in hm and hm[str.split(' ')[i]] != pattern[i]:
                return False
            elif not str.split(' ')[i] in hm:
                hm[str.split(' ')[i]] = pattern[i]
        return True           

    return False



pattern = 'abba'
str = "dog cat cat fish"
print(wordPattern(pattern, str))