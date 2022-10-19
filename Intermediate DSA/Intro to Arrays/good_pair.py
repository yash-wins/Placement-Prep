# Given an array A and an integer B. A pair(i, j) in the array is a good pair if i != j and (A[i] + A[j] == B). Check if any good pair exist or not.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        for i in range(len(A)):
            for j in range(len(A)):
                if i != j and A[i] + A[j] == B:
                    return 1
        return 0