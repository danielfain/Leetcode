def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    l = s.split()
    for i in range(len(l)):
        l[i] = l[i][::-1]
    return ' '.join(l)


s = "Let's take LeetCode contest"
print(reverseWords(s))
