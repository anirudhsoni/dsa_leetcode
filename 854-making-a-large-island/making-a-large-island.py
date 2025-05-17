class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        moves=[[0,1],[1,0],[-1,0],[0,-1]]
        parent={}
        area={}

        def dfs(r,c,p):
            if (r,c) in parent:
                return 0
            parent[(r,c)]=p
            res=1
            for a,b in moves:
                if -1<r+a<len(grid) and -1<c+b<len(grid[0]) and grid[r+a][c+b]==1:
                    res+=dfs(r+a,c+b,p)
            return res

        zeros=set()

        mxArea=1

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in parent and grid[r][c]==1:
                    area[(r,c)]=dfs(r,c,(r,c))
                    mxArea=max(mxArea,area[(r,c)])
                if grid[r][c]==0:
                    zeros.add((r,c))

        def getUnionArea(r,c):
            A=1
            curParents=set()
            for a,b in moves:
                if -1<r+a<len(grid) and -1<c+b<len(grid[0]) and grid[r+a][c+b]==1:
                    if parent[(r+a,c+b)] not in curParents:
                        A+=area[parent[(r+a,c+b)]]
                        curParents.add(parent[(r+a,c+b)])
            return A

        for zero in zeros:
            mxArea=max(mxArea,getUnionArea(zero[0],zero[1]))

        return mxArea
            


        
