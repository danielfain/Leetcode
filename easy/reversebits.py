class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        b = [i for i in bin(n)[2:]]
        b.reverse()
        t = ''.join(b) + (abs(len(b) - 32) * '0')
        return int(t, 2)
        