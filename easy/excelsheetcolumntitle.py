def convertToTitle(n):
    t = ''
    while n > 0:
        t += chr(65 + (n-1) % 26)
        n = (n - 1) // 26
        
    return t[::-1]


n = 704
print(convertToTitle(n))