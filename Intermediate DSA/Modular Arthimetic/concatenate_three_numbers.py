# Given three 2-digit integers, A, B, and C, find out the minimum number obtained by concatenating them in any order.

# Return the minimum result obtained.

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        if A>=B and A>=C:
            if B>=C:
                return int(str(C)+str(B)+str(A))
            else:
                return int(str(B)+str(C)+str(A))
        elif B>=A and B>=C:
            if A>=C:
                return int(str(C)+str(A)+str(B))
            else:
                return int(str(A)+str(C)+str(B))
        elif C>=A and C>=B:
            if A>=B:
                return int(str(B)+str(A)+str(C))
            else:
                return int(str(A)+str(B)+str(C))
            
#alternate solution
class Solution:
    def solve(self, A, B, C):
        return int(''.join([str(x) for x in sorted([A, B, C])]))
