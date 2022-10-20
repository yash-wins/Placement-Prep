# You are given a string S, and you have to find all the amazing substrings of S.

# An amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        B = [0 for i in range(len(A))]
        for i in range(len(A)):
            ch = A[i]
            if (ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U'):
                B[i] = len(A)-i
                B[i] += B[i-1]
            else:
                B[i] = B[i-1]
        return int(B[len(A)-1] % 10003)