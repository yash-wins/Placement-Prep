# Given an integer array A of size N. In one second, you can increase the value of one element by 1.

# Find the minimum time in seconds to make all elements of the array equal.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        max = 0
        for i in range(len(A)):
            if max < A[i]:
                max = A[i]
        count = 0
        for j in range(len(A)):
            diff = max - A[j]
            count += diff
        return count

