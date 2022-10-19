# Given an integer array A of size N and an integer B, you have to return the same array after rotating it B times towards the right.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        N = len(A)
        B = B % N
        reverse(A, 0, N - 1);
        reverse(A, 0, B - 1);
        reverse(A, B, N - 1);
        return A

def reverse(A, start, end):
    i, j = start, end
    while(i < j):
        temp = A[i]
        A[i] = A[j]
        A[j] = temp
        i, j = i + 1, j - 1