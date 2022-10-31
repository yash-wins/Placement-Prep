# You are given a number A. You are also given a base B. A is a number on base B.
# You are required to convert the number A into its corresponding value in decimal number system.

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        i = 0
        ans = 0
        while A>0:
            ans = ans + (A%10)*(B**i)
            A = A//10
            i += 1
        return ans