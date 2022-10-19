# You are given a constant array A.

# You are required to return another array which is the reversed form of the input array.

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def solve(self, A):
        B = A[::-1]
        return B