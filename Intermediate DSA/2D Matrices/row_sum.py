# You are given a 2D integer matrix A, return a 1D integer array containing row-wise sums of original matrix.

class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        B = []
        for i in range(len(A)):
            sum = 0
            for j in range(len(A[0])):
                sum += A[i][j]
            B.append(sum)
        return B