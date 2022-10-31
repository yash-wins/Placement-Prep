# Given an array of integers A and multiple values in B, which represents the number of times array A needs to be left rotated.

# Find the rotated array for each value and return the result in the from of a matrix where ith row represents the rotated array for the ith value in B.

# Problem Constraints
# 1 <= length of both arrays <= 2000 -10^9 <= A[i] <= 10^9 0 <= B[i] <= 2000

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        n = len(A)
        a2 = []
        for i in range(len(B)):
            B[i] = B[i]%n
            a1 = [0 for i in range(n)]
            a1[:] = A[B[i]:n] + A[0:B[i]]
            a2.append(a1)
        return a2