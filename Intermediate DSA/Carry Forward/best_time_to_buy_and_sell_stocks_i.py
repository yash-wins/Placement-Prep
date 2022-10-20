# Say you have an array, A, for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Return the maximum possible profit.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        greatest_on_right = 0
        profit = 0
        for i in range(len(A) - 1, -1, -1):
            greatest_on_right = max(A[i], greatest_on_right)
            profit = max(profit, greatest_on_right - A[i])
        return profit
