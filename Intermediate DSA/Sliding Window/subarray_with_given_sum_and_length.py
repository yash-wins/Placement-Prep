# Given an array A of length N. Also given are integers B and C.
# Return 1 if there exists a subarray with length B having sum C and 0 otherwise

class Solution:
    # @param num : list of integers
    # @param B : integer
    # @param target : integer
    # @return an integer
    def solve(self, nums, B, target):
        windowSum = 0
        (low, high) = (0, 0)
        for low in range(len(nums)):
            while windowSum < target and high < len(nums):
                windowSum += nums[high]
                high = high + 1
            if windowSum == target:
                if high-low==B:
                    return 1
            windowSum -= nums[low]
        return 0
