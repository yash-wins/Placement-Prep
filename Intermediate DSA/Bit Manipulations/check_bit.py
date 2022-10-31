# You are given two integers A and B.
# Return 1 if B-th bit in A is set
# Return 0 if B-th bit in A is unset

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if A & (1<<B):
            return 1
        else:
            return 0