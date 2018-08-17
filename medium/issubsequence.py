def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    c = 0
    if s == "":
        return True
    
    for letter in t:
        if letter == s[c]:
            c += 1
            if c == len(s):
                return True
    return False







s = ""
t = "ahbgdc"
print(isSubsequence(s, t))
    