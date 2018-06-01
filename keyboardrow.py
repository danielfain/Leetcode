def findWords(words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        l = []
        top_row = 'qwertyuiop'
        mid_row = 'asdfghjkl'
        bot_row = 'zxcvbnm'

        for word in words:
            r = None
            d = None
            
            if word[0].lower() in top_row:
                r = top_row
            elif word[0].lower() in mid_row:
                r = mid_row
            elif word[0].lower() in bot_row:
                r = bot_row
            
            for letter in word:
                if letter.lower() in r:
                    d = True
                else:
                    d = False
                    break
            
            if d == True:
                l.append(word)
                
        return l


words = ["Hello", "Alaska", "Dad", "Peace"]
print(findWords(words))