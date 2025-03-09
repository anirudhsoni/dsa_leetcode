class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def Pow(x,n):
            # print(x,n)
            if n==0:
                return 1
            elif n&1==0:
                return Pow(x*x,n//2)
            return x*Pow(x,n-1)
        
        return Pow(x,n) if n>0 else 1/Pow(x,-1*n)
        
        