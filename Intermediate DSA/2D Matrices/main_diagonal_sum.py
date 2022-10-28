# e given a N X N integer matrix. You have to find the sum of all the main diagonal elements of A.

# Main diagonal of a matrix A is a collection of elements A[i, j] such that i = j.

class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):
        sum = 0
        for i in range(len(A)):
            sum += A[i][i]
        return sum