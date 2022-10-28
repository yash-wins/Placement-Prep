# You are given a N X N integer matrix. You have to find the sum of all the minor diagonal elements of A.

# Minor diagonal of a M X M matrix A is a collection of elements A[i, j] such that i + j = M + 1 (where i, j are 1-based).

class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):
        ans = 0
        for i in range(1,len(A)+1):
            for j in range(1,len(A)+1):
                if i+j == len(A)+1:
                    ans += A[i-1][j-1]
        return ans