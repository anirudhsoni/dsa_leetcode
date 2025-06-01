class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp={c:1 for c in coins}
        dp[0]=0

        def dfs(i):
            if i<0:
                return float('infinity')
            if i in dp:
                return dp[i]
            res=float('infinity')
            for c in coins:
                res=min(res,1+dfs(i-c))
            dp[i]=res
            return dp[i]
        
        res=dfs(amount)
        return res if res!=float('infinity') else -1