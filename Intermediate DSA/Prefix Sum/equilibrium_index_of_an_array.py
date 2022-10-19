# You are given an array A of integers of size N.

# Your task is to find the equilibrium index of the given array

# The equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.
# NOTE:
# Array indexing starts from 0.
# If there is no equilibrium index then return -1.
# If there are more than one equilibrium indexes then return the minimum index.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        leftsum = 0
        rgtsum = sum(A)
        for i in range(n):
            rgtsum -= A[i]
            if rgtsum == leftsum:
                return i
            leftsum += A[i]
        return -1
