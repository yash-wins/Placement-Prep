# Given an array of integers A, a subarray of an array is said to be good if it fulfills any one of the criteria:
# 1. Length of the subarray is be even, and the sum of all the elements of the subarray must be less than B.
# 2. Length of the subarray is be odd, and the sum of all the elements of the subarray must be greater than B.
# Your task is to find the count of good subarrays in A.

# Problem Constraints
# 1 <= len(A) <= 10^3
# 1 <= A[i] <= 10^3
# 1 <= B <= 10^7

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        c = 0
        for i in range(n):
            s = 0
            l = 0
            for j in range(i,n):
                l = j - i + 1
                s += A[j]
                if l%2==0:
                    if s < B:
                        c+=1
                else:
                    if s > B:
                        c+=1
        return c