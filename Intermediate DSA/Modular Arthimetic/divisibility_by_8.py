# You are given a number A in the form of a string. Check if the number is divisible by eight or not.

# Return 1 if it is divisible by eight else, return 0.

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        if int(A)%8==0:
            return 1
        else:
             return 0