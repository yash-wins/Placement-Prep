# You are given an array A of length N and Q queries given by the 2D array B of size Q*2. Each query consists of two integers B[i][0] and B[i][1].
# For every query, the task is to calculate the sum of all even indices in the range A[B[i][0]…B[i][1]].

# Note : Use 0-based indexing

class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        C = [0 for i in range(len(B))]
        for i in range(2,len(A),2):
            A[i] += A[i-2]
            A[i-1] = 0
        
        if((len(A)-1) % 2 != 0 ):
            A[len(A)-1] = 0
            
        for i in range(1,len(A),2):  
            A[i] = A[i-1]
        
        for i in range(len(B)):
            val = 0
            if(B[i][0]!=0):
                val = A[B[i][0]-1];
            C[i] = A[B[i][1]] - val
        return C
