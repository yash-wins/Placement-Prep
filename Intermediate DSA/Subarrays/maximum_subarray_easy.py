# You are given an integer array C of size A. Now you need to find a subarray (contiguous elements) so that the sum of contiguous elements is maximum.
# But the sum must not exceed B.

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def maxSubarray(self, A, B, C):
        ans = 0
        for i in range(A):
            s = 0
            for j in range(i,A):
                s += C[j]
                if s <= B:
                    ans = max(s,ans)
                else:
                    break
        return ans