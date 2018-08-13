import string

def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    w = string.ascii_lowercase + string.digits
    low = ''.join(s.lower().split())
    sentence = ''.join([l for l in low if l in w])
    start = 0
    end = len(sentence) - 1

    while end > start:
    	if sentence[start] == sentence[end]:
    		start += 1
    		end -= 1
    	else:
    		return False
    return True

    

    


s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))