# Given an array of size N, find the subarray of size K with the least average.

class Solution:
    # @return an integer
    def solve(self, arr, k):
        n = len(arr)
        min = 999999
        minindex = 0
        for i in range(n-k+1):
            sum = 0
            j = i
            for j in range(i, i+k):
                sum += arr[j]
            if sum < min:
                min = sum
                minindex = i
        return minindex