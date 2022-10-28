# You are given two matrices A & B of same size, you have to return another matrix which is the sum of A and B.

class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        n = len(A)
        m = len(A[0])
        C = [[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                C[i][j] = A[i][j] + B[i][j]
        return C
