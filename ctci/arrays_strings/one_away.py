def one_away(string1, string2):             # O(n) time and O(n) space
    if string1 == string2: return True
    
    hm1 = {}

    for char in string1:
        if char in hm1:
            hm1[char] = hm1.get(char) + 1
        else:
            hm1[char] = 1

    hm2 = {}

    for char in string2:
        if char in hm2:
            hm2[char] = hm2.get(char) + 1
        else:
            hm2[char] = 1

    num_diffs = 0

    for char in string2:
        if char in hm1:
            if hm1.get(char) != hm2.get(char): 
                num_diffs += 1
        else:
            num_diffs += 1

    return num_diffs <= 1


# TODO There is a O(n) time and O(1) solution    

string1 = "pale"
string2 = "ple"
print(one_away(string1, string2))