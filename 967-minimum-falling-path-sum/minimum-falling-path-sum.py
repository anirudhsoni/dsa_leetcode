class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        def dfs(r,c):
            if not 0<=c<len(matrix[0]):
                return float('infinity')
            if r==len(matrix):
                return 0
            if (r,c) in cache:
                return cache[(r,c)]
            
            cache[(r,c)] = matrix[r][c]+min(dfs(r+1,c),dfs(r+1,c-1),dfs(r+1,c+1))
            return cache[(r,c)]

        res=float('infinity')
        cache={}
        for i in range(len(matrix[0])):
            res=min(res,dfs(0,i))

        return res