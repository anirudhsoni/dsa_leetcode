class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj={i:set() for i in range(n)}

        for a,b,w in flights:
            adj[a].add((b,w))
        
        vst=set()
        h=[]
        h.append([0,src,k])
        mincost=float('infinity')
        while h:
            # print(h,vst)
            totalcost,node,stopsleft=heapq.heappop(h)
            if node==dst and stopsleft>=-1:
                mincost=min(mincost,totalcost)
            if (node,stopsleft) not in vst and stopsleft>=0:
                vst.add((node,stopsleft))
                for child,ticket in adj[node]:
                    heapq.heappush(h,[totalcost+ticket,child,stopsleft-1])
        return mincost if mincost!=float('infinity') else -1

        