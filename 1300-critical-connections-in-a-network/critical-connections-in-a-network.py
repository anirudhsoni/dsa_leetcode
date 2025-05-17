class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        adj={i:set() for i in range(n)}

        for a,b in connections:
            adj[a].add(b)
            adj[b].add(a)
        
        time={}
        critical=[]

        def dfs(n,parent,t):
            if n in time:
                return
            time[n]=[t,t]
            for child in adj[n]:
                if child!=parent:
                    dfs(child,n,t+1)
            for child in adj[n]:
                if child!=parent:
                    time[n][1]=min(time[n][1],time[child][1])

            if time[parent][1]<time[n][1]:
                critical.append([parent,n])
            return

        dfs(0,0,0)
        
        return critical