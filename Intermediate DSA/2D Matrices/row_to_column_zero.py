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

    
#Alternate Solution
class Soln:
    def solve(self, A):
        n = len(A)
        m = len(A[0])
        for i in range(0,n):
            flag = 0
            for j in range(0,m):
                if A[i][j] == 0:
                    flag = 1
            if flag == 1:
                for j in range(0,m):
                    if A[i][j] != 0:
                        A[i][j] = -1
        for j in range(0,m):
            flag = 0
            for i in range(0,n):
                if A[i][j] == 0:
                    flag = 1
            if flag == 1:
                for i in range(0,n):
                    if A[i][j] != 0:
                        A[i][j] = -1
        for i in range(0,n):
            for j in range(0,m):
                if A[i][j] == -1: A[i][j] = 0
        return A
