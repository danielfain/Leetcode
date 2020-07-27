def palindrome_permutations(string):        # O(n) time and O(n) space
    string = string.lower()
    string = string.replace(" ", "")

    hm = {}

    for char in string:
        if char in hm:
            hm[char] = hm.get(char) + 1
        else:
            hm[char] = 1

    if len(string) % 2 == 1:
        num_odds = 0
        for num in hm.values():
            if num % 2 == 1:
                num_odds += 1

            if num_odds > 1: 
                return False
    
    if len(string) % 2 == 0:
        for num in hm.values():
            if num % 2 == 1:
                return False

    return True


string = "NASA at a santa"
print(palindrome_permutations(string))