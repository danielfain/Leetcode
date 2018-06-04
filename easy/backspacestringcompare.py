def backspaceCompare(S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s = ['' for i in range(S.count('#'))]
        t = ['' for i in range(T.count('#'))]
        for letter in S:
            if letter != '#':
                s.append(letter)
            else:
                del s[-1]
        for letter in T:
            if letter != '#':
                t.append(letter)
            else:
                del t[-1]
        
        if ''.join(s) == ''.join(t):
            return True
        else:
            return False



S = "e##e#o##oyof##q"
T = "e##e#fq##o##oyof##q"
print(backspaceCompare(S, T))