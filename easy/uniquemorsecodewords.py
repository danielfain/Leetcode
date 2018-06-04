from string import ascii_lowercase

class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse_trans = []

        for word in words:
            w = ''
            for letter in word:
                w += morse[ascii_lowercase.index(letter)]
            morse_trans.append(w)

        return len(set(morse_trans))



words = ["gin", "zen", "gig", "msg"] # Input a list of words
print(Solution.uniqueMorseRepresentations(Solution(), words))

#beats 100% of python3 submissions