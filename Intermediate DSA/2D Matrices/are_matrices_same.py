# Problem Description
# You are given two matrices A & B of equal dimensions and you have to check whether two matrices are equal or not.

# NOTE: Both matrices are equal if A[i][j] == B[i][j] for all i and j in the given range.

class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        a = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]==B[i][j]:
                    a = 1
                else:
                    a = 0
                    break
        return a
