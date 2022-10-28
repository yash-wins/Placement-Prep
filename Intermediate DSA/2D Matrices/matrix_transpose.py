# You are given a matrix A, you have to return another matrix which is the transpose of A.

# NOTE: Transpose of a matrix A is defined as - AT[i][j] = A[j][i] ; Where 1 ≤ i ≤ col and 1 ≤ j ≤ row. The tranpose of a matrix switches the element at (i, j)th index to (j, i)th index, and the element at (j, i)th index to (i, j)th index.

class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        B = []
        for i in range(len(A[0])):
            temp = []
            for j in range(len(A)):
                temp.append(A[j][i])
            B.append(temp)
        return B