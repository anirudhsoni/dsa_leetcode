class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        

        def dfs(r,c):
            if r>=len(triangle):
                return 0
            if c>=len(triangle[r]):
                return float('infinity')
            
            if (r,c) in cache:
                return cache[(r,c)]
            cache[(r,c)]=triangle[r][c] + min(dfs(r+1,c),dfs(r+1,c+1))
            return cache[(r,c)]

        cache={}
        return dfs(0,0)