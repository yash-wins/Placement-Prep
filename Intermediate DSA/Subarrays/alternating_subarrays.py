# You are given an integer array A of length N comprising of 0's & 1's, and an integer B.

# You have to tell all the indices of array A that can act as a center of 2 * B + 1 length 0-1 alternating subarray.

# A 0-1 alternating array is an array containing only 0's & 1's, and having no adjacent 0's or 1's. For e.g. arrays [0, 1, 0, 1], [1, 0] and [1] are 0-1 alternating, while [1, 1] and [0, 1, 0, 0, 1] are not.

# Problem Constraints
# 1 <= N <= 10^3
# A[i] equals to 0 or 1.
# 0 <= B <= (N - 1) / 2

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        l1 = []
        n = len(A)
        length = 2 * B + 1
        for i in range(n - length + 1):
            curr = -1
            flag = 1
            for j in range(i, i + length):
                if (A[j] == curr):
                    flag = 0
                    break
                curr = A[j]
            if (flag == 1):
                l1.append(i + B)
        return l1