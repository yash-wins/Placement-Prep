# You are given an integer array A.

# Decide whether it is possible to divide the array into one or more subarrays of even length such that the first and last element of all subarrays will be even.

# Return "YES" if it is possible; otherwise, return "NO" (without quotes).


class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        n = len(A)
        if n%2==0:
            for i in range(n):
                for j in range(i,n):
                    if A[i]%2==0 and A[n-1]%2==0:
                        return "YES"
                    else:
                        return "NO"
        else:
            return "NO"            