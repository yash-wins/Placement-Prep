# Given an array A of N integers. Count the number of elements that have at least 1 elements greater than itself.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        max = A[0]
        for i in range(0,n):
            if max < A[i]:
                max = A[i]
        for i in range(n):
            if max == A[i]:
                n = n -1
        return n