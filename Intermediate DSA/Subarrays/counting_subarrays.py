# Given an array A of N non-negative numbers and a non-negative number B,
# you need to find the number of subarrays in A with a sum less than B.
# We may assume that there is no overflow.

# Problem Constraints
# 1 <= N <= 10^3
# 1 <= A[i] <= 1000
# 1 <= B <= 10^7

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count = 0
        n = len(A)        
        for i in range(n):
            s = 0
            for j in range(i,n):
                s += A[j]
                if s < B:
                    count += 1
        return count
                