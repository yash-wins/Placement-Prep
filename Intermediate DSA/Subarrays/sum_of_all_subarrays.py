# You are given an integer array A of length N.
# You have to find the sum of all subarray sums of A.
# More formally, a subarray is defined as a contiguous part of an array which we can obtain by deleting zero or more elements from either end of the array.
# A subarray sum denotes the sum of all the elements of that subarray.

class Solution:
    # @param A : list of integers
     # @return an long
    def subarraySum(self, A):
        res = 0
        n = len(A)
        for i in range(0,n):
            res += (A[i] * (i+1) * (n-i))
        return res