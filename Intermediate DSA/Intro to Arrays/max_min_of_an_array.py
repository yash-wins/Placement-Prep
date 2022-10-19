# Given an array A of size N. You need to find the sum of Maximum and Minimum element in the given array.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        min = A[0]
        max = A[0]
        for i in range(len(A)):
            if min > A[i]:
                min = A[i]
            elif max < A[i]:
                max = A[i]
        return max + min