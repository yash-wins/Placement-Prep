# Given an array of integers A and an integer B, find and return the minimum number of swaps required to bring all the numbers less than or equal to B together.

# Note: It is possible to swap any two elements, not necessarily consecutive.

class Solution:
    # @param arr : list of integers
    # @param k : integer
    # @return an integer
    def solve(self, arr, k):
        n = len(arr)
        count = 0
        for i in range(0, n) :
            if (arr[i] <= k) :
                count = count + 1
        bad = 0
        for i in range(0, count) :
            if (arr[i] > k) :
                bad = bad + 1
        ans = bad
        j = count
        for i in range(0, n) :      
            if(j == n) :
                break
            if (arr[i] > k) :
                bad = bad - 1
            if (arr[j] > k) :
                bad = bad + 1
            ans = min(ans, bad)
            j = j + 1
        return ans
