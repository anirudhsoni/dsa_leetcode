class Solution:
    def climbStairs(self, n: int) -> int:
        a,b=1,1
        if n<2:
            return a
        for i in range(1,n):
            a,b=b,a+b
        return b
