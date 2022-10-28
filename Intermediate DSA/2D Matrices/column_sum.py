# You are given a 2D integer matrix A, return a 1D integer array containing column-wise sums of original matrix.

class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        B = []
        for i in range(len(A[0])):
            sum = 0
            for j in range(len(A)):
                sum += A[j][i]
            B.append(sum)
        return B