# Given two integers A and B. Find the minimum value (A ⊕ X) + (B ⊕ X) that can be achieved for any X.

# where P ⊕ Q is the bitwise XOR operation of the two numbers P and Q.

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        x = A & B
        return (A ^ x) + (B ^ x)