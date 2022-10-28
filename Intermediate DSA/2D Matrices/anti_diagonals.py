# Give a N * N square matrix A, return an array of its anti-diagonals. Look at the example for more details.

class Solution:


    def diagonal(self, A):
        ans = []
     for i in range(2 * len(A) - 1) :
         if i < len(A) :
             z = 0
         else :
             z = i - len(A) + 1
         temp = []
         for j in range(z, i - z + 1) :
             temp.append(A[j] [i - j])
            for k in range(0,z):
                temp.append(0)
            for k in range(i - z + 1, len(A)):
                temp.append(0)
         ans.append(temp)
     return ans
