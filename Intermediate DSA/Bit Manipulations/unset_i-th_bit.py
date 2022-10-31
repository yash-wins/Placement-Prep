# You are given two integers A and B.
# If B-th bit in A is set, make it unset
# If B-th bit in A is unset, leave it as it is
# Return the updated A value

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if A & (1<<B):
            A = A ^ (1<<B)
        return A