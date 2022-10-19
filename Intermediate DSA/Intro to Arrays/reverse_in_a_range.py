# Given an array A of N integers. Also given are two integers B and C. Reverse the array A in the given range [B, C]

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        temp = 0
        while C >= B:
            temp = A[B]
            A[B]=A[C]
            A[C]= temp
            B += 1
            C -= 1
        return A