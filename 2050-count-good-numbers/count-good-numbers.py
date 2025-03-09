class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod=10**9 + 7
        def expo(x : int , n : int) -> int:
            nonlocal mod
            if n==0:
                return 1
            elif n&1==0:
                return expo( x ** 2 % mod , n // 2)
            return x * expo( x , n-1) % mod

        return 5 ** (n % 2) * expo(20 , n // 2) % mod
        
        