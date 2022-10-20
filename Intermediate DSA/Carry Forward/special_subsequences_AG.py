# You have given a string A having Uppercase English letters.

# You have to find how many times subsequence "AG" is there in the given string.

# NOTE: Return the answer modulo 109 + 7 as the answer can be very large.

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        b = 0
        c = 0
        for i in range(len(A)):
            if A[i]=='A':
                c += 1
            elif A[i]=='G':
                b += c
        return b
