class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache={}
        def dfs(i,sm):
            if sm == amount:
                return 1
            if i>=len(coins) or sm>amount:
                return 0
            if (i,sm) in cache:
                return cache[(i,sm)]
            cache[(i,sm)] = dfs(i,sm+coins[i])+dfs(i+1,sm)
            return cache[(i,sm)]
        return dfs(0,0)