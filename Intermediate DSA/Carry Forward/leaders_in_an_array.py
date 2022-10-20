# Given an integer array A containing N distinct integers, you have to find all the leaders in array A.

# An element is a leader if it is strictly greater than all the elements to its right side.

# NOTE:The rightmost element is always a leader.

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        a = []
        temp = 0
        for i in range(len(A)):
            temp = A[i]
            for j in range(i,len(A)):
                if temp<A[j]:
                    temp = A[j]
            if temp==A[i]:
                a.append(A[i])
        return a

