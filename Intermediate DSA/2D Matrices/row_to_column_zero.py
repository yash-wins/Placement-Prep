# You are given a 2D integer matrix A, make all the elements in a row or column zero if the A[i][j] = 0. Specifically, make entire ith row and jth column zero.

class Soln:
    def solve(self, A):
        r = []
        c = []
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]==0:
                    r.append(i)
                    c.append(j)
        for i in range(len(r)):
            i = r[i]
            for j in range(len(A)):
                A[i][j] = 0
        for i in range(len(c)):
            i = c[i]
            for j in range(len(A[0])):
                A[j][i] = 0
        return A
