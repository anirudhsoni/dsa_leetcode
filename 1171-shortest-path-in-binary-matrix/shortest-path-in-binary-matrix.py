class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1:
            return -1
        
        dist=[[float('infinity') for i in range(len(grid[0]))] for j in range(len(grid))]
        parent=[[(i,j) for i in range(len(grid[0]))] for j in range(len(grid))]
        dist[0][0]=1

        moves=[[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
        # print(dist,parent)

        q=deque()
        q.append((0,0))

        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                for R,C in moves:
                    if -1<r+R<len(grid) and -1<c+C<len(grid[0]) and grid[r+R][c+C]==0:
                        d=dist[r][c]+1
                        if d<dist[r+R][c+C]:
                            dist[r+R][c+C]=d
                            parent[r+R][c+C]=(r,c)
                            q.append((r+R,c+C))
        
        return dist[-1][-1] if dist[-1][-1]!=float('infinity') else -1