# Given an array A, find the size of the smallest subarray such that it contains at least one occurrence of the maximum value of the array

# and at least one occurrence of the minimum value of the array.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        ma, mi, a, b = 0, 0, 0, 0
        for i in range(len(A)):
            if ma < A[i]:
                ma = A[i]
                a = i
            elif mi > A[i] or mi==0:
                mi = A[i]
                b = i
        if b-a>0:
            return b-a
        else:
            return a-b
