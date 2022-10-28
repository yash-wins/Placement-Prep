# You are given a n x n 2D matrix A representing an image.
# Rotate the image by 90 degrees (clockwise).
# You need to do this in place.
# Note: If you end up using an additional array, you will only receive partial score.

class Solution:
    def solve(self, matrix):
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp
        return matrix
