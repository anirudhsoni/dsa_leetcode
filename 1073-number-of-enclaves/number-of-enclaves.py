class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        moves=[[0,1],[1,0],[0,-1],[-1,0]]
        
        def dfs(r,c):
            if grid[r][c]==0 or grid[r][c]==2:
                return
            grid[r][c]=2
            for R,C in moves:
                if -1<r+R<len(grid) and -1<c+C<len(grid[0]):
                    dfs(r+R,c+C)
            return

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if r==0 or c==0 or r==len(grid)-1 or c==len(grid[0])-1:
                    # print(r,c)
                    dfs(r,c)

        res=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    res+=1
        return res

        