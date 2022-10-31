# Given an integer A representing a year, Return 1 if it is a leap year else, return 0.

# A year is a leap year if the following conditions are satisfied:

# The year is multiple of 400.
# or the year is multiple of 4 and not multiple of 100.

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        B = int(A)
        if B%400==0:
            return 1
        else:
            if B%4==0 and B%100!=0:
                return 1
        return 0