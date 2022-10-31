# You are given two integers A and B.
# If B-th bit in A is set, make it unset
# If B-th bit in A is unset, make it set
# Return the updated A value

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        return A ^ (1<<B)
