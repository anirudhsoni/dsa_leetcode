class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        dp={}

        def dfs(l,r):
            if (l,r) in dp:
                return dp[(l,r)]
            if r-l==1:
                return 0
            
            res=float('inf')

            for cut in cuts:
                if l<cut<r:
                    res=min(res,r-l+dfs(l,cut)+dfs(cut,r))
            if res==float('inf'):
                res=0
            dp[(l,r)]=res
            return res

        return dfs(0,n)