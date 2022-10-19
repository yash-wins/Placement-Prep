# You are given an integer array A of length N.
# You are also given a 2D integer array B with dimensions M x 2, where each row denotes a [L, R] query.
# For each query, you have to find the sum of all elements from L to R indices in A (1 - indexed).
# More formally, find A[L] + A[L + 1] + A[L + 2] +... + A[R - 1] + A[R] for each query.

class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        C = []
        L,R = 0,0
        for i in range(0,len(B)):
            sum = 0
            L = B[i][0]-1
            R = B[i][1]
            for j in range(L,R):
                sum += A[j]
            C.append(sum)
        return C