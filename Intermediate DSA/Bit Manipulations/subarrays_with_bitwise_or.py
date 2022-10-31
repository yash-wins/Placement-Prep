# Given an array B of length A with elements 1 or 0. Find the number of subarrays with bitwise OR 1.

class Solution:
    # @param A : integer
    # @param B : list of integers
     # @return an long
    def solve(self, A, B):
        count = 0
        for i in range(A):
            for j in range(i,A):
                if B[i] | B[j]:
                    count += 1
        return count