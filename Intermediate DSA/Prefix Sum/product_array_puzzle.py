# Given an array of integers A, find and return the product array of the same size where the ith element of the product array will be equal to the product of all the elements divided by the ith element of the array.

# Note: It is always possible to form the product array with integer (32 bit) values. Solve it without using the division operator.

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = 1
        B = [0 for i in range(len(A))]
        for i in range(len(A)):
            n = n*A[i]
        for i in range(len(A)):
            B[i] = int(n/(A[i]))
        return B