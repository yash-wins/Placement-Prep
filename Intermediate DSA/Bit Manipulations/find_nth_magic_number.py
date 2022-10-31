# Given an integer A, find and return the Ath magic number.
# A magic number is defined as a number that can be expressed as a power of 5 or a sum of unique powers of 5.
# First few magic numbers are 5, 25, 30(5 + 25), 125, 130(125 + 5), ….

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        pow = 1
        ans = 0
        while A>0:
            pow = pow*5
            if A & 1:
                ans += pow
            A >>= 1
        return ans