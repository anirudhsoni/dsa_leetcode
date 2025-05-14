class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        adj=[[float('infinity') for i in range(n)] for j in range(n)]
        # print(adj)

        for i in range(n):
            adj[i][i]=0

        for a,b,d in edges:
            adj[a][b]=d
            adj[b][a]=d

        for i in range(n):
            for r in range(n):
                if r==i:
                    continue
                for c in range(n):
                    if c==i:
                        continue
                    adj[r][c]=min(adj[r][c],adj[r][i]+adj[i][c])

        # print(adj)

        res=[0,float('infinity')]
        for r in range(n):
            # print(res,r)
            city=0
            for c in range(n):
                # print(r,c)
                if 0<adj[r][c]<=distanceThreshold:
                    city+=1
            if res[1]>=city:
                res=[r,city]

        return res[0]
        
        



        