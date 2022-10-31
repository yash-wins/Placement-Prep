# You are given two integers A and B.
# Set the A-th bit and B-th bit in 0, and return output in decimal.

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        a = (1<<A) | (1<<B)
        return a
