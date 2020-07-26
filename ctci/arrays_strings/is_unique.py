def is_unique(string): # O(n) time and O(n) space
    hm = {}

    for char in string:
        if char in hm:
            return False
        else:
            hm[char] = True

    return True


def is_unique2(string): # O(n^2) time and O(1) space
    for i in range(len(string) - 1):            # O(n)
        for j in range(i + 1, len(string)):     # O(n)
            if string[i] == string[j]:
                return False

    return True


def is_unique3(string): # O(n) time and O(1) space
    if len(string) > 128: return False          # there are only 128 ascii characters

    char_vals = [False for _ in range(128)]

    for char in string:
        ord_val = ord(char)

        if char_vals[ord_val]:
            return False
        else:
            char_vals[ord_val] = True

    return True


words = ["abcde", "hello", "apple", "kite", "padle"]
for word in words:
    print(word + ": " + str(is_unique3(word)))


# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?