def mostCommonWord(paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        punc = "!?',;."
        l = []
        for letter in list(paragraph):
            if not letter in punc:
                l.append(letter.lower())

        p = ''.join(l).split(' ')
        m = 0
        w = ''
        for word in set(p):
            if not word in banned:
                if p.count(word) > m:
                    m = p.count(word)
                    w = word
        return w
        
        

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(mostCommonWord(paragraph, banned))