# Given a decimal number A and base B.
# You are required to change the decimal number A into the corresponding value in base B and return that.

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def DecimalToAnyBase(self, A, B):
        ans = 0
        i = 0
        while A > 0:
            ans = ans + (A%B)*(10**i)
            A = A//(B)
            i+=1
        return ans