# You are given an integer array A of size N.
# You have to pick B elements in total. Some (possibly 0) elements from left end of array A and some (possibly 0) from the right end of array A to get the maximum sum.
# Find and return this maximum possible sum.
# NOTE: Suppose B = 4, and array A contains 10 elements, then
# You can pick the first four elements or can pick the last four elements, or can pick 1 from front and 3 from the back, etc. You need to return the maximum possible sum of elements you can pick.


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        cpt = 0
        maxpt = 0
        for i in range(B):
            cpt += A[i]
        maxpt = cpt
        j = len(A) - 1
        for  i in range(B-1,-1,-1):
            cpt = cpt + A[j] - A[i]
            maxpt = max(cpt , maxpt)
            j -= 1
        return maxpt