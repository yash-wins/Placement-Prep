# You are given an integer array A of length N.
# You are also given a 2D integer array B with dimensions M x 2, where each row denotes a [L, R] query.
# For each query, you have to find the sum of all elements from L to R indices in A (1 - indexed).
# More formally, find A[L] + A[L + 1] + A[L + 2] +... + A[R - 1] + A[R] for each query.

class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
     # @return an list of long
    def rangeSum(self, A, B):
        n, m = len(A), len(B)
        pref = [0 for i in range(n + 1)]
        for i in range(1, n + 1):
            pref[i] = pref[i - 1] + A[i - 1]   
        ans = [0 for i in range(m)]
        for i in range(m):
            ans[i] = pref[B[i][1]] - pref[B[i][0] - 1]
        return ans