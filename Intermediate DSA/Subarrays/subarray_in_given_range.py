# Given an array A of length N, return the subarray from B to C.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        d = []
        for i in range(B,C+1):
            d.append(A[i])
        return d