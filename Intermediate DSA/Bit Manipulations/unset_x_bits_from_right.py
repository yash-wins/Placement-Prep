# Given an integer A. Unset B bits from the right of A in binary.
# For eg:-
# A = 93, B = 4
# A in binary = 1011101
# A should become = 1010000 = 80. Therefore return 80.

class Solution:
    # @param A : long
    # @param B : integer
     # @return an long
    def solve(self, A, B):
        for i in range(B):
            if A & (1<<i):
                A = A ^ (1<<i)
        return A