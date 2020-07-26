def check_permutation(string1, string2):            # O(n) time and O(n) space
    if len(string1) != len(string2) or string1 == string2: return False

    hm = {}

    for char in string1:
        hm[char] = True

    for char in string2:
        if not char in hm:
            return False

    return True


def check_permutation2(string1, string2):           # O(n^2) time and O(1) space
    if len(string1) != len(string2) or string1 == string2: return False

    for char in string1:
        if not char in string2:
            return False

    return True


def check_permutation3(string1, string2):           # O(n log n) time and O(1) space
    if len(string1) != len(string2) or string1 == string2: return False

    if sorted(string1) != sorted(string2):
        return False

    return True


string1 = "abc"
string2 = "bac"
print(check_permutation2(string1, string2))

# Given two strings, write a method to decide if one is a permutation of the other.