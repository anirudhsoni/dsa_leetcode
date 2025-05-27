class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        R=len(obstacleGrid)
        C=len(obstacleGrid[0])
        cache={}
        def dfs(r,c):
            nonlocal R,C
            if r>=R or c>=C or obstacleGrid[r][c]==1:
                return 0
            if r==R-1 and c==C-1:
                return 1
            if (r,c) in cache:
                return cache[(r,c)]
            cache[(r,c)] = dfs(r+1,c)+dfs(r,c+1)
            return cache[(r,c)]

        return dfs(0,0)