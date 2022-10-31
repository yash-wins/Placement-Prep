# Reverse the bits of an 32 bit unsigned integer A.

class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        B = 0
        for i in range(32):
            if A & (1<<i):
                B = B | (1<<(31-i))
        return B