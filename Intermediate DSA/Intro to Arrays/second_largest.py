# You are given an integer array A. You have to find the second largest element/value in the array or report that no such element exists.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        max = A[0]
        n = len(A)
        A.sort()
        if len(A)>1:
            max = A[n-2]
        else:
            max = -1
        return max